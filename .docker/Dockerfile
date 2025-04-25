FROM odoo:16

USER root

# Definir el directorio de trabajo (opcional pero recomendado)
WORKDIR /opt/odoo

# Copiar el requirements.txt al contenedor
COPY requirements.txt .

# Actualizar pip e instalar las dependencias desde requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
RUN mkdir -p /var/log/odoo && touch /var/log/odoo/odoo.log

USER odoo
