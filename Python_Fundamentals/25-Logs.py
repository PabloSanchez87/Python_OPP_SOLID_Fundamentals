# LOGS
""" 
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 """
import logging
import time
 
                            ###############
                            ## EJERCICIO ##
                            ###############
#  * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
#  * un ejemplo con cada nivel de "severidad" disponible.

# Congiguración de logging
logging.basicConfig(level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler()])

# Severity
logging.debug("Mensaje de DEBUG")
logging.info("Mensaje de INFO")
# Por defecto sólo imprime los logs de warning, error y critical.
logging.warning("Mensaje de WARNING")
logging.error("Mensaje de ERROR")
logging.critical("Mensaje de CRITICAL")
                    
                            ###############
                            ##   EXTRA   ##
                            ###############
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
#  * y listar dichas tareas.
#  * - Añadir: recibe nombre y descripción.
#  * - Eliminar: por nombre de la tarea.
#  * Implementa diferentes mensajes de log que muestren información según la
#  * tarea ejecutada (a tu elección).
#  * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.                            
print("·"*50)

def execution_time(func):
    """
    Decorador para medir y registrar el tiempo de ejecución de una función.
    Args:
        func (callable): La función a la que se aplicará el decorador.
    Returns:
        callable: Una nueva función que envuelve la función original y mide su tiempo de ejecución.
    """
    def wrapper(*args, **kwargs):
        """
        Envuelve la función original y mide su tiempo de ejecución.
        Args:
            *args: Argumentos posicionales para la función decorada.
            **kwargs: Argumentos nombrados para la función decorada.
        Returns:
            El resultado de la función decorada.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.debug(
            f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos.")
        return result
    return wrapper


class TaskManager:
    def __init__(self) -> None:
        self.tasks = {}
    
    @execution_time
    def add_task(self, name:str, description:str):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f" --> Tarea añadida: {name}")       
        else:
            logging.warning(f" --> La tarea no ha sido añadido: {name}.")
        logging.debug(f"Número de tareas: {len(self.tasks)}")
        
        
        
    @execution_time    
    def delete_task(self, name:str):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f" --> Tarea eliminada: {name}")
        else:
            logging.error(f" --> No se ha eliminado la tarea: {name}.")
        logging.debug(f"Número de tareas: {len(self.tasks)}")    
        
        
    @execution_time    
    def list_task(self):
        if self.tasks:
            logging.info(f" --> Tareas listadas:")
            for name, description in self.tasks.items():
                print(f" · {name} - {description}")
        else:
            logging.info(f" --> No hay tareas para imprimir.")
                
    
    @execution_time
    def _print_time(self, star_time, end_time):
        logging.debug(
            f"Tiempo de ejecución: {end_time - star_time:.6f} segundos.")
        



# Ejemplo de uso.
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.list_task()
    task_manager.add_task("Desayuno", "Preparar el desayuno.")
    task_manager.add_task("Programar", "Programar las tareas del día.")
    task_manager.list_task()
    task_manager.delete_task("Desayuno")
    task_manager.delete_task("Desayuno")
    task_manager.list_task()
    task_manager.add_task("Programar", "Programar las tareas del día.")