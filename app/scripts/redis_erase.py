import redis

def clear_redis_database(
        
    host='5.161.194.3', 
    port=5438, 
    password='jouuvVr3wsN0U8fh9OCPnUeAgmuPpZTBiPEiKxDjjY2O2PdILQzzM4hszD6oPWEK', 
    db=0, 
    namespace=None
):
    """
    Limpia una base de datos Redis.
    
    Args:
        host: Hostname del servidor Redis
        port: Puerto del servidor Redis
        password: Contraseña (si es necesaria)
        db: Número de base de datos a limpiar
        namespace: Si se proporciona, solo elimina las claves con este prefijo
    """
    # Conectar a Redis
    r = redis.Redis(
        host=host,
        port=port,
        password=password,
        db=db,
        decode_responses=True  # Para ver las claves como strings
    )
    
    # Verificar conexión
    try:
        r.ping()
        print(f"Conectado exitosamente al servidor Redis en {host}:{port}, DB {db}")
    except redis.ConnectionError as e:
        print(f"Error de conexión: {e}")
        return False
    
    # Contar claves antes de borrar
    if namespace:
        pattern = f"{namespace}*"
        keys = r.keys(pattern)
        key_count = len(keys)
        print(f"Se encontraron {key_count} claves con el prefijo '{namespace}'")
        
        # Borrar claves con el prefijo específico
        if key_count > 0:
            # Usar pipeline para operaciones por lotes
            pipe = r.pipeline()
            for key in keys:
                pipe.delete(key)
            pipe.execute()
            print(f"Eliminadas {key_count} claves con prefijo '{namespace}'")
    else:
        # Contar claves totales
        key_count = len(r.keys())
        print(f"Se encontraron {key_count} claves en la base de datos {db}")
        
        # Borrar todas las claves (flushdb)
        r.flushdb()
        print(f"Base de datos {db} ha sido limpiada completamente")
    
    # Verificar que se eliminaron las claves
    remaining = len(r.keys(namespace + "*" if namespace else "*"))
    print(f"Claves restantes: {remaining}")
    
    # Cerrar conexión
    r.close()
    
    return True

# Ejemplo de uso:
if __name__ == "__main__":
    # Para borrar toda la base de datos
    clear_redis_database()
    
    # Para borrar solo las claves con un prefijo específico
    # clear_redis_database(namespace="pdf_documents")
    
    # Para conectarse a un servidor Redis remoto
    # clear_redis_database(host="redis.example.com", port=6379, password="secretpassword", db=0)