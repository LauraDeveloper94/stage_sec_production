---
layout: default
title: "Comunicación entre módulos"
description: "Muestra la relación que tiene el módulo de producción con otros módulos de Odoo"
date: 2025-02-16
---

- **Fabricación - Compras**: Después de realizar un pedido, se genera una orden de producción que se envía al departamento de producción.
- **Fabricación - Ventas**: El sistema detecta que no hay suficiente inventario y solicita la aprobación del departamento de compras.
- **Fabricación - Inventario**: Si hay existencias, se notifica al departamento de producción.
- **Fabricación - Facturación**: Al completar la producción, se emite una factura con los datos necesarios.
- **Fabricación - Contabilidad**: Se registran horas y costos para generar los asientos contables correspondientes.
