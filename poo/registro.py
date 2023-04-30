import subprocess as sp
import tkinter as tk
from tkinter import BOTH, W, Toplevel, ttk
from tkinter.messagebox import NO
from tkinter import *
import sqlite3 as sql




class MainWindow:
   
    
    def __init__(self,ventana):
       
       
        self.ventana=ventana
        self.ventana.geometry('865x515')
        
        self.ventana.resizable(width=False, height=False)
        self.ventana.title('Registro de datos')
        self.frame=tk.Frame(self.ventana)
        self.frame.pack(fill=BOTH, expand=True)
        self.ventana = self.centra(self.ventana,865,515)

        self.frame_label= tk.Frame(self.ventana, width= 310,height=270, borderwidth=3, relief="sunken")
        self.frame_label.place(x=4, y= 85)

    
        self.label_registro=tk.Label(self.frame, text='Registro', font='Helvetica 17 bold')
        self.label_registro.place(x=125, y=30)
        

        self.label_identificacion=tk.Label(self.frame_label, text='Identificación:')
        self.label_identificacion.place(x=5, y=10)

        self.label_nombre=tk.Label(self.frame_label, text='Nombre:')
        self.label_nombre.place(x=5, y=50)

        self.label_direccion=tk.Label(self.frame_label, text='Dirección:')
        self.label_direccion.place(x=5, y=90)

        self.label_celular=tk.Label(self.frame_label, text='Celular:')
        self.label_celular.place(x=5, y=130)

        self.label_empresa=tk.Label(self.frame_label, text='Empresa')
        self.label_empresa.place(x=5, y=170)

        self.label_evento=tk.Label(self.frame_label, text='Evento')
        self.label_evento.place(x=5, y=210) 

        self.label_mensajes=tk.Label(self.frame_label, text='', font='Helvetica 10')
        self.label_mensajes.place(x=30, y=240)

        "Creación y ubicación de los entry"
        self.entry_identificacion=tk.Entry(self.frame_label,font='Helvetica 10')
        self.entry_identificacion.place(x=90, y=10, width= 200)
        self.entry_identificacion.focus()
        self.entry_identificacion.bind("<Key>",self.identific)
        self.entry_identificacion.bind("<BackSpace>",  self.entry_identificacion.delete(len(self.entry_identificacion.get()),END))
        
        self.entry_nombre=tk.Entry(self.frame_label, font='Helvetica 10')
        self.entry_nombre.place(x=90, y=50, width= 200)
        
        self.entry_direccion=tk.Entry(self.frame_label,font='Helvetica 10')
        self.entry_direccion.place(x=90, y=90, width= 200)

        self.entry_celular=tk.Entry(self.frame_label, font='Helvetica 10')
        self.entry_celular.place(x=90, y=130, width= 200)
        self.entry_celular.bind("<Key>", self.nume)
        self.entry_celular.bind("<BackSpace>", lambda _:self.entry_celular.delete(len(self.entry_celular.get()),END))


        self.entry_empresa=tk.Entry(self.frame_label, font='Helvetica 10')
        self.entry_empresa.place(x=90, y=170, width= 200)
        
        self.entry_evento=tk.Entry(self.frame_label, font='Helvetica 10')
        self.entry_evento.place(x=90, y=210, width= 200)
        "creación y ubicación de los botones"
        self.button_agregar=tk.Button(self.frame, text='Grabar', width=9, command= self.agregar)
        self.button_agregar.place(x=9, y=390)

  

        self.button_editar=tk.Button(self.frame, text='Editar', width=9, command= self.editar)
        self.button_editar.place(x=85,y=390)

        self.button_eliminar=tk.Button(self.frame, text='Eliminar', width=9, command= self.eliminar)
        self.button_eliminar.place(x=161, y=390)

        self.button_cancelar= tk.Button(self.frame, text= 'Cancelar', width=9, command= self.cancelar)
        self.button_cancelar.place(x=237, y=390)

        "Creación  y ubicación del tree-view, donde irán apareciendo la información suministrada"
        self.tree_view=ttk.Treeview(self.ventana, height=17)
        self.tree_view['columns']=('ID','NOMBRE', 'DIRECCIÓN','CELULAR','EMPRESA','EVENTO' )
        self.tree_view.column('#0',width=0, stretch=NO, minwidth=0) 
        self.tree_view.column('ID',anchor=W,width=82) #82
        self.tree_view.column('NOMBRE', anchor=W,width=83)
        self.tree_view.column('DIRECCIÓN', anchor=W,width=83)
        self.tree_view.column('CELULAR', anchor=W, width=82)#82
        self.tree_view.column('EMPRESA', anchor=W, width=83)
        self.tree_view.column('EVENTO', anchor=W, width=83)

        self.tree_view.heading('#0',text='', anchor=W)
        self.tree_view.heading('ID',text='ID', anchor=W)
        self.tree_view.heading('NOMBRE',text='NOMBRE', anchor=W)
        self.tree_view.heading('DIRECCIÓN',text='DIRECCIÓN', anchor=W)
        self.tree_view.heading('CELULAR',text='CELULAR', anchor=W)
        self.tree_view.heading('EMPRESA',text='EMPRESA', anchor=W)
        self.tree_view.heading('EVENTO',text='EVENTO', anchor=W)
        self.tree_view.place(x=320,y=85)
        self.editar_bool= False

        cone=sql.connect("info.db")
        cur=cone.cursor()
        select = cur.execute("select * from informacion")
        for row in select:
            self.tree_view.insert('',END,values=row)
       
        
    
    def agregar(self): 

     try:



      cone=sql.connect("info.db")
      cur=cone.cursor()
      identi= self.entry_identificacion.get()
      orden=f"select id from informacion where id = {identi}"
      ejecutar = cur.execute(orden)
      datoid = cur.fetchone()
    
      cone.commit()
      cone.close()
     
      if self.editar_bool== False:
        if datoid == None:

          
           conn=sql.connect("info.db")
           cursor=conn.cursor()
           instruccion=f"INSERT INTO informacion VALUES ({self.entry_identificacion.get()},'{self.entry_nombre.get()}','{self.entry_direccion.get()}',{self.entry_celular.get()},'{self.entry_empresa.get()}','{self.entry_evento.get()}')"
           cursor.execute(instruccion)
           conn.commit()
           conn.close() 
           self.tree_view.insert(parent='', index='end', text='', values=(self.entry_identificacion.get(),self.entry_nombre.get(), self.entry_direccion.get(), self.entry_celular.get(), self.entry_empresa.get(), self.entry_evento.get()))

           self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
           self.frame_label1.place(x=300, y= 465)
           self.label_mensajes=tk.Label(self.frame_label1, text='Información guardada con exito')
           self.label_mensajes.place(x=50, y=5)
           self.label_mensajes.config(fg="green")
           self.entry_celular.delete(0,END)
           self.entry_direccion.delete(0,END)
           self.entry_empresa.delete(0,END)
           self.entry_evento.delete(0,END)
           self.entry_nombre.delete(0,END)
           #self.sleep(0.1)
           #self.entry_identificacion.config(state="normal")
           self.entry_identificacion.delete(0,END) 
        elif datoid[0]==int(identi):
           
           self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") 
           self.frame_label1.place(x=300, y= 465)
           self.label_mensajes=tk.Label(self.frame_label1, text='La identificación ya existe')
           self.label_mensajes.place(x=50, y=5)
           self.label_mensajes.config(fg="red")
           self.entry_celular.delete(0,END)
           self.entry_direccion.delete(0,END)
           self.entry_empresa.delete(0,END)
           self.entry_evento.delete(0,END)
           self.entry_nombre.delete(0,END)
           self.entry_identificacion.delete(0,END) 
            


      elif self.editar_bool == True:
           id=self.tree_view.item(self.tree_view.selection())['values'][0]
           identificacion= self.entry_identificacion.get()
           nombre=self.entry_nombre.get()
           direccion=self.entry_direccion.get()
           celular=self.entry_celular.get()
           empresa=self.entry_empresa.get()
           evento=self.entry_evento.get()       
           conn=sql.connect("info.db")
           cursor=conn.cursor()
           instruccion=f"UPDATE informacion SET id={identificacion},nombre='{nombre}',direccion='{direccion}',celular={celular},empresa='{empresa}',evento='{evento}' WHERE id= {id}"
           cursor.execute(instruccion)
           conn.commit()
           conn.close() 
           selected=self.tree_view.focus()
           self.tree_view.item(selected, text='', values=(identificacion,nombre,direccion,celular,empresa,evento))
           self.editar_bool= False
           self.entry_identificacion.config(state="normal")
           self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
           self.frame_label1.place(x=300, y= 465)
           self.label_mensajes=tk.Label(self.frame_label1, text='Información actualizada con exito')
           self.label_mensajes.place(x=50, y=5)
           self.label_mensajes.config(fg="green")
           self.entry_celular.delete(0,END)
           self.entry_direccion.delete(0,END)
           self.entry_empresa.delete(0,END)
           self.entry_evento.delete(0,END)
           self.entry_nombre.delete(0,END)
           self.entry_identificacion.delete(0,END)
     except:
        self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken")
        self.frame_label1.place(x=300, y= 465)
        self.label_mensajes=tk.Label(self.frame_label1, text='Debe llenar todos los campos \n   para grabar un registro')
        self.label_mensajes.place(x=50, y=5)
        self.label_mensajes.config(fg="red")

        return
        
     
     
       


    def identific(self,event):
        '''limita caracteres de identificacion '''
        if event.char:
            if len(self.entry_identificacion.get()) >= 15:
                self.entry_identificacion.delete(14,END)
                self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
                self.frame_label1.place(x=300, y= 465)
                self.label_mensajes=tk.Label(self.frame_label1, text='Máximo 15 caracteres')
                self.label_mensajes.place(x=50, y=5)
                self.label_mensajes.config(fg="red")
        ''' Valida la identificación '''
        if event.char.isdigit():
            return self.entry_identificacion
        else:
            self.entry_identificacion.delete(14,END)
            self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
            self.frame_label1.place(x=300, y= 465)
            self.label_mensajes=tk.Label(self.frame_label1, text='Solo números para la identificacion')
            self.label_mensajes.place(x=50, y=5)
            self.label_mensajes.config(fg="red")
            self.entry_identificacion.delete(0,END)
            return "break" 


    def nume(self,event):
        '''limita caracteres de identificacion '''
        if event.char:
            if len(self.entry_celular.get()) >= 10:
                self.entry_celular.delete(9,END)
                self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
                self.frame_label1.place(x=300, y= 465)
                self.label_mensajes=tk.Label(self.frame_label1, text='Máximo 10 números')
                self.label_mensajes.place(x=50, y=5)
                self.label_mensajes.config(fg="red")
        ''' Valida el celular '''
        if event.char.isdigit():
            return self.entry_celular
        else:
            #self.entry_celular.delete(0,END)
            self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
            self.frame_label1.place(x=300, y= 465)
            self.label_mensajes=tk.Label(self.frame_label1, text='Solo números para el celular')
            self.label_mensajes.place(x=50, y=5)
            self.label_mensajes.config(fg="red")
            self.entry_celular.delete(0,END)
            return "break"


    def eliminar(self):
        try:
            self.tree_view.item(self.tree_view.selection())['values'][0]
            self.entry_celular.delete(0,END)
            self.entry_direccion.delete(0,END)
            self.entry_empresa.delete(0,END)
            self.entry_evento.delete(0,END)
            self.entry_nombre.delete(0,END)
            self.entry_identificacion.config(state="normal")
            self.entry_identificacion.delete(0,END) 
            self.editar_bool= False
            self.label_mensajes.destroy() 
            

        except:
            self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
            self.frame_label1.place(x=300, y= 465)
            # self.label_mensajes['text']='Seleccione el elemento que\n   quiera eliminar'
            self.label_mensajes=tk.Label(self.frame_label1, text='Seleccione el elemento que\n   desea eliminar')
            self.label_mensajes.place(x=50, y=5) #posicion del texto dentro del Frame
            self.label_mensajes.config(fg="red") #color del texto
            return
        id=self.tree_view.item(self.tree_view.selection())['values'][0]
        conn=sql.connect("info.db")
        cursor=conn.cursor()
        instruccion=f"DELETE from informacion WHERE id ={id} "
        cursor.execute(instruccion)
        conn.commit()
        conn.close() 
        self.tree_view.delete(self.tree_view.selection()[0])
        self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken") #creacion del frame para advertencias
        self.frame_label1.place(x=300, y= 465)
        self.label_mensajes=tk.Label(self.frame_label1, text='Información eliminada con exito')
        self.label_mensajes.place(x=50, y=5)
        self.label_mensajes.config(fg="green")
       
    

    def centra(self,win,ancho,alto): 
        """ centra las ventanas en la pantalla """ 
        x = win.winfo_screenwidth() // 2 - ancho // 2 
        y = win.winfo_screenheight() // 2 - alto // 2 
        win.geometry(f'{ancho}x{alto}+{x}+{y}') 

    def cancelar(self):
          self.entry_celular.delete(0,END)
          self.entry_direccion.delete(0,END)
          self.entry_empresa.delete(0,END)
          self.entry_evento.delete(0,END)
          self.entry_nombre.delete(0,END)
          self.entry_identificacion.config(state="normal")
          self.entry_identificacion.delete(0,END) 
          self.editar_bool= False
          self.label_mensajes.destroy()

    def editar(self):
        self.cancelar()
        try:
            self.tree_view.item(self.tree_view.selection())['values'][0]
            self.label_mensajes.destroy() 
        except:
            self.frame_label1= tk.Frame(self.ventana, width= 250,height=97, relief="sunken")
            self.frame_label1.place(x=300, y= 465)
            self.label_mensajes=tk.Label(self.frame_label1, text='Seleccione el elemento que\n   desea editar')
            self.label_mensajes.place(x=50, y=5)
            self.label_mensajes.config(fg="red")
            
           
            return   
         
        self.editar_bool= True

        id= self.tree_view.item(self.tree_view.selection())['values'][0]
        self.entry_identificacion.insert(0,f'{id}')
        self.entry_identificacion.config(state="readonly")
        #NOMBRE
        nombre= self.tree_view.item(self.tree_view.selection())['values'][1]
        self.entry_nombre.insert(0,f"{nombre}")
        #DIRECCION
        direccion= self.tree_view.item(self.tree_view.selection())['values'][2]
        self.entry_direccion.insert(0,f"{direccion}")


        #CELULAR
        celular= self.tree_view.item(self.tree_view.selection())['values'][3]
        self.entry_celular.insert(0,f"{celular}")


        #EMPRESA
        empresa= self.tree_view.item(self.tree_view.selection())['values'][4]
        self.entry_empresa.insert(0,f"{empresa}")


        #EVENTO
        evento= self.tree_view.item(self.tree_view.selection())['values'][5]
        self.entry_evento.insert(0,f"{evento}")

        




      
    "para crear la base de datos:"
    def create_db():
            conn=sql.connect("info.db")
            conn.commit()
            conn.close()
    "para crear la tabla de la base de datos:"
    def create_table():
            conn=sql.connect("info.db")
            cursor=conn.cursor()
            cursor.execute(
                """CREATE TABLE informacion (
                    id integer,
                    nombre text,
                    direccion text,
                    celular integer, 
                    empresa text,
                    evento text
                ) """
            )
            conn.commit()
            conn.close() 



if __name__=='__main__':
    cls=sp.call('cls',shell=True)
  
    # update_fields()
    win=tk.Tk()
    app=MainWindow(win)
    
    win.mainloop()


