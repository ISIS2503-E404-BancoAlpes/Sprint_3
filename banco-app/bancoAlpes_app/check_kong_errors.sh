#!/bin/bash

LOG_FILE="/var/log/kong/error.log"  # Ajustar la ruta de configuración
SEARCH_PATTERN="error"  # Ajustar el error que se busca
EMAIL="andresfcord@gmail.com"  # Correo para mandar notificación
SUBJECT="Error Alert from Kong"
TEMP_FILE="/tmp/kong_errors_found.log"

# Se verifica si existe el archivo
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found: $LOG_FILE"
    exit 1
fi

# Busca el error deseado en el log
grep "$SEARCH_PATTERN" "$LOG_FILE" > "$TEMP_FILE"

# Verifica si hay contenido en el archivo temporal
if [ -s "$TEMP_FILE" ]; then
    # Si se encuentra un error se envia el correo
    mail -s "$SUBJECT" "$EMAIL" < "$TEMP_FILE"
fi

rm "$TEMP_FILE"
