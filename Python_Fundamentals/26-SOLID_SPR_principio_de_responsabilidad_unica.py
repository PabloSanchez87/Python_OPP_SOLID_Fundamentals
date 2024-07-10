# SPR - Principio de responsabilidad única.
""" 
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 *  1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 *      información básica como título, autor y número de copias disponibles.
 *  2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 *      información básica como nombre, número de identificación y correo electrónico.
 *  3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 *      tomar prestados y devolver libros.
 * Instrucciones:
 *  1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 *      los tres aspectos mencionados anteriormente (registro de libros, registro de
 *      usuarios y procesamiento de préstamos).
 *  2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 *      siguiendo el Principio de Responsabilidad Única.
"""

""" Teoría - SPR - Single Responsibility Principle"""
# Cada clase tiene una única responsabilidad. 
# Cada clase tiene una única razón para cambiar.
    # Si la clase tiene más de una responsabilidad, si una cambia podría romper
    #   nuestro código.
""""""   

                            ###############
                            ## EJERCICIO ##
                            ###############                           
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
#  * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.

# Incorrecto
class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        
    def save_to_database(self):
        pass
    
    def send_email(self):
        pass
    
    ## Tiene dos responsabilidades, guardar en database y otra enviar el email.
    ## Tanto guardar como enviar deberían ser independientes de la clase User.


# Correcto
class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

class UserRepository:
    def save_to_database(self, user:User):
        pass

class EmailService:
    def send_email(self, email, message):
        pass

    ## Estamos modelando de manera independientes.

                     
                            ###############
                            ##   EXTRA   ##
                            ###############
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
#  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
#  * y el procesamiento de préstamos de libros.
#  * Requisitos:
#  *  1. Registrar libros: El sistema debe permitir agregar nuevos libros con
#  *      información básica como título, autor y número de copias disponibles.
#  *  2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
#  *      información básica como nombre, número de identificación y correo electrónico.
#  *  3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
#  *      tomar prestados y devolver libros.
#  * Instrucciones:
#  *  1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
#  *      los tres aspectos mencionados anteriormente (registro de libros, registro de
#  *      usuarios y procesamiento de préstamos).
#  *  2. Refactoriza el código: Separa las responsabilidades en diferentes clases
#  *      siguiendo el Principio de Responsabilidad Única.

# Incorrecto
class Library:
    
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = []
            
    def add_book(self,title, author,copies):
        self.books.append({"title": title, "author": author, "copies": copies})
        
    def add_user(self, name, id, email):
        self.users.append({"name": name, "id": id, "email": email})
        
    def loan_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -=1
                self.loans.append({"user_id": user_id, "book_title": book_title})
                return True
        return False
    
    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] +=1
                    return True
        return False
    # Cada cambio repercute directamente en los demás métodos.                
    
    
# Correcto

# Responsabilidad: Representar un libro con sus atributos.
# Comentario: Encapsula la información de un libro y no realiza ninguna otra operación.
class Book:
    def __init__(self, title, author, copies):
        """
        Inicializa un objeto Book con un título, un autor y un número de copias disponibles.
        
        :param title: El título del libro.
        :param author: El autor del libro.
        :param copies: El número de copias disponibles del libro.
        """
        self.title = title
        self.author = author
        self.copies = copies
        
        
# Responsabilidad: Representar un usuario con sus atributos.
# Comentario: Encapsula la información de un usuario y no realiza ninguna otra operación.    
class Users:
    def __init__(self, nombre, id, email):
        """
        Inicializa un objeto User con un nombre, una identificación y un correo electrónico.
        
        :param nombre: El nombre del usuario.
        :param id: La identificación del usuario.
        :param email: El correo electrónico del usuario.
        """
        self.nombre = nombre
        self.id = id
        self.email = email
        
      
# Responsabilidad: Gestionar los préstamos de libros.
# Comentario: Contiene la lógica para prestar y devolver libros. No gestiona directamente los 
#     datos de los libros o usuarios fuera del contexto de los préstamos.  
class Loan:
    def __init__(self) -> None:
        """
        Inicializa el servicio de préstamos con una lista vacía de préstamos.
        """
        self.loans = []
        
    def loan_book(self, user: Users, book: Book) -> bool:
        """
        Método para prestar un libro a un usuario.
        
        :param user: El usuario que solicita el préstamo.
        :param book: El libro que se desea prestar.
        :return: True si el préstamo fue exitoso, False en caso contrario.
        """
        if book.copies > 0:  # Comprueba si hay copias disponibles.
            book.copies -= 1  # Reduce el número de copias disponibles.
            self.loans.append({"user_id": user.id, "book_title": book.title})  # Registra el préstamo.
            return True
        return False
        
    def return_book(self, user: Users, book: Book) -> bool:
        """
        Método para devolver un libro prestado.
        
        :param user: El usuario que devuelve el libro.
        :param book: El libro que se desea devolver.
        :return: True si la devolución fue exitosa, False en caso contrario.
        """
        for loan in self.loans:  # Busca el préstamo en la lista de préstamos.
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)  # Elimina el préstamo de la lista.
                book.copies += 1  # Incrementa el número de copias disponibles.
                return True
        return False

# Responsabilidad: Gestionar la colección de libros y usuarios, y coordinar los préstamos 
#     utilizando el servicio de préstamos (Loan).
# Comentario: Administra la colección de libros y usuarios, y delega la lógica de préstamos 
#     a la clase Loan. 
#     Esto sigue el SRP ya que la clase Library no se encarga de los detalles de cómo se prestan 
#         y devuelven los libros, sino que coordina las acciones utilizando otras clases.
class Library:
    def __init__(self) -> None:
        """
        Inicializa la biblioteca con listas vacías de libros y usuarios, y un servicio de préstamos.
        """
        self.books = []
        self.users = []
        self.loans_service = Loan()
            
    def add_book(self, book: Book):
        """
        Añade un libro a la lista de libros de la biblioteca.
        
        :param book: El libro a añadir.
        """
        self.books.append(book)
        
    def add_user(self, user: Users):
        """
        Añade un usuario a la lista de usuarios de la biblioteca.
        
        :param user: El usuario a añadir.
        """
        self.users.append(user)
        
    def loan_book(self, user_id: int, book_title: str) -> bool:
        """
        Método para prestar un libro a un usuario específico.
        
        :param user_id: La identificación del usuario.
        :param book_title: El título del libro que se desea prestar.
        :return: True si el préstamo fue exitoso, False en caso contrario.
        """
        
        """ 
        u for u in self.users if u.id == user_id:
            Esta es una comprensión de generador que itera sobre cada usuario u en self.users.
        if u.id == user_id 
            es una condición que filtra los usuarios y solo selecciona aquel cuyo id coincida con user_id.
        next(...):
            La función next() se utiliza para obtener el siguiente (en este caso, el único) 
            elemento del generador.
                Si el generador encuentra un usuario cuyo id coincide con user_id, 
                    next() devolverá ese usuario.
            Si no se encuentra ningún usuario que cumpla con la condición, next() devuelve None 
                (el segundo argumento de next), indicando que no se encontró ningún usuario con ese id.
        """
        user = next((u for u in self.users if u.id == user_id), None)  # Busca al usuario por ID.
        book = next((b for b in self.books if b.title == book_title), None)  # Busca el libro por título.
        
        if user and book:
            return self.loans_service.loan_book(user, book)  # Usa el servicio de préstamos para prestar el libro.
        
        return False
        
    def return_book(self, user_id: int, book_title: str) -> bool:
        """
        Método para devolver un libro prestado por un usuario específico.
        
        :param user_id: La identificación del usuario.
        :param book_title: El título del libro que se desea devolver.
        :return: True si la devolución fue exitosa, False en caso contrario.
        """
        user = next((u for u in self.users if u.id == user_id), None)  # Busca al usuario por ID.
        book = next((b for b in self.books if b.title == book_title), None)  # Busca el libro por título.
        
        if user and book:
            return self.loans_service.return_book(user, book)  # Usa el servicio de préstamos para devolver el libro.
        
        return False


""" 
Clase Book y Users tienen responsabilidades claras y únicas.
Clase Loan maneja exclusivamente la lógica de préstamos y devoluciones.
Clase Library coordina la gestión de libros, usuarios y la lógica de préstamos sin involucrarse 
    en los detalles de la implementación de los préstamos.
"""

    

    
