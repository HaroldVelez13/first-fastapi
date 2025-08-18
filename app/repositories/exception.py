from fastapi import HTTPException, status

class DatabaseError(HTTPException):
    """Excepción genérica para errores de base de datos."""
    def __init__(self, detail: str = "Ocurrió un error en la base de datos."):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)

class DuplicateEntryError(HTTPException):
    """Excepción para violaciones de unicidad."""
    def __init__(self, detail: str = "El recurso ya existe."):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)