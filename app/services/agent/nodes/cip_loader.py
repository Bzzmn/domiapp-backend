from typing_extensions import Annotated
from langgraph.prebuilt import InjectedState
from langgraph.types import Command

def cip_loader(state: Annotated[dict, InjectedState]) -> Command:
    """
    This function retrieves the project cip data from the database.
    """

    cip_id = "ff35c0abc1e163f"
    cip_numero = "415" 
    cip_fecha = "2023-08-18"
    calle = "AV. EINSTEIN"
    loteo = "VILLA HERMOSA"
    manzana = "22"
    lote = "66"
    rol = "3173-028"
    numero_asignado = "264"

    identificacion_propiedad = {
        "cip_id": cip_id,
        "cip_numero": cip_numero,
        "cip_fecha": cip_fecha,
        "calle": calle,
        "loteo": loteo,
        "manzana": manzana,
        "lote": lote,
        "rol": rol,
        "numero_asignado": numero_asignado,
    }

    plan_intercomunal_o_metropolitano = "P.R.M.S y sus modificaciones vigentes, fecha diario oficial 11-02-2010"
    plan_regulador_comunal = "Res N 104 de fecha 22.11.2004, fecha diario oficial 08-01-2005"
    mod_1_plano_regulador_comunal = "Res N 2591 Exento de fecha 27.06.2012, fecha diario oficial 10-08-2012"
    mod_2_plano_regulador_comunal = "Dec N 555 Exento de fecha 12.03.2018, fecha diario oficial 16-03-2018"
    area_de_ubicacion = "Urbana"

    instrumentos_aplicables = {
        "plan_intercomunal_o_metropolitano": plan_intercomunal_o_metropolitano,
        "plan_regulador_comunal": plan_regulador_comunal,
        "mod_1_plano_regulador_comunal": mod_1_plano_regulador_comunal,
        "mod_2_plano_regulador_comunal": mod_2_plano_regulador_comunal,
        "area_de_ubicacion": area_de_ubicacion,
    }

    debe_acompanar_informe_calidad_subsuelo = True

    zona_emplazamiento = "U - EH : “MEXICO CENTRO”"
    usos_permitidos = """
        Residencial: Vivienda, Hospedaje. 
        Equipamiento: De toda las clases y escalas establecidas con excepción de los prohibidos. Centros de servicio automotriz, establecimiento de Venta Minorista de Combustibles Líquidos. 
        Actividades Productivas:  
            -Taller: Taller, Taller Mecánico, los que deben cumplir con las condiciones detalladas en el Cuadro N°2 A de esta Ordenanza. 
            -Industria, Actividades Productivas de Carácter Industrial, Servicios de Carácter Industrial, las que deben cumplir con las condiciones detalladas en el Cuadro 
            N°2 A de esta Ordenanza. 
            -Almacenamiento: Bodega, la que debe cumplir con las disposiciones contempladas en el Cuadro N°2 B de la presente Ordenanza. 
        Infraestructura: Energética. 
        Espacio Público. 
        Área verde.
        """
    usos_prohibidos = "Se prohíben todos los usos que no estén expresamente permitidos."
    zona_o_subzona_edificacion_emplazamiento = "E-M1: MÉXICO CENTRO Y PONIENTE, DORSAL, SUR Y AV. GUANACO"
    superficie_de_subdivision_predial_minima = "600 m2"
    densidad_maxima_de_poblacion = "1200 HAB/HA"
    densidad_minima_de_poblacion = "100 HAB/HA"
    altura_maxima_de_edificacion_contino_pareado = "7 m"
    altura_maxima_de_edificacion_aislado = "20 m"
    sistema_de_agrupamiento = """
        CONTÍNUO HASTA LA ALTURA MÁXIMA 
        PERMITIDA Y AISLADA EN PISOS SUPERIORES. 
        PAREADO HASTA ALTURA MÁXIMA PERMITIDA Y 
        AISLADA EN PISOS SUPERIORES. AISLADO.
        """
    coeficiente_de_constructibilidad = "1.6"
    coeficiente_de_ocupacion_de_suelo = """
        CONTINUO-PAREADO: 0.6 
        AISLADO: 0.4 
        """
    ocupacion_pisos_superiores = """
        0.6 HASTA LOS 7 MT. 
        0.4 SOBRE LOS 7 MT.
        """
    rasante = """
        2.6.3 OGUC Y  
        3.3.5 DE LA 
        ORDENANZA LOCAL
        """
    nivel_de_aplicacion = """
        2.6.3 OGUC Y  
        3.3.5 DE LA ORDENANZA 
        LOCAL
        """
    adosamientos = "ART. 2.6.2 OGUC"
    distanciamiento = """
        2.6.3 OGUC Y  
        3.3.5 DE LA 
        ORDENANZA 
        LOCAL
        """
    cierros_hacia_espacio_publico_3_3_8_prr_altura = "2.50 MT"
    cierros_hacia_espacio_publico_3_3_8_prr_transparencia = "50% MIN."
    cierros_hacia_espacio_publico_3_3_9_prr_altura_minima = "2.00M"
    cierros_hacia_espacio_publico_3_3_9_prr_altura_maxima = "2.50M"
    ochavos = "4.00 MT (ART. 2.5.4 OGUC) "
    antejardin = "3.0 MT."
    normas_urbanisticas_especiales = """
        - Independientemente de la información entregada en el presente certificado, el solicitante deberá considerar la totalidad de los artículos contenidos en la Ordenanza 
        Local y sus Modificaciones. 
        Párrafo 3.1: Normas generales sobre Loteamientos y Urbanizaciones. 
        Párrafo 3.2: Normas generales sobre Uso de Suelo. 
        Párrafo 3.3: Normas generales sobre Subdivisión, Ocupación de Suelo y Edificación. 
        Párrafo 5.2: Estacionamientos. 
        -Las distancias entre líneas oficiales aquí indicadas, corresponden a las existentes frente a la propiedad consultada. 
        -Las zonas de uso de suelo y de edificación aquí indicadas, corresponden a las definidas por la unidad SIG de esta DOM, en concordancia con los planos físicos aprobados 
        (PRR01 y PRR02)
        """
    exigencias_estacionamiento = "DEBERÁ CUMPLIR CON EL ARTICULO 5.2.4 (TITULO V) DEL P.R.R. "
    area_de_riesgo = False
    area_de_proteccion = False
    zona_o_inmueble_conservacion_historica = False
    zona_tipica_o_monumento_nacional = False

    usos_de_suelo = {
        "zona_emplazamiento": zona_emplazamiento,
        "usos_permitidos": usos_permitidos,
        "usos_prohibidos": usos_prohibidos,
        "zona_o_subzona_edificacion_emplazamiento": zona_o_subzona_edificacion_emplazamiento,
        "superficie_de_subdivision_predial_minima": superficie_de_subdivision_predial_minima,
        "densidad_maxima_de_poblacion": densidad_maxima_de_poblacion,
        "densidad_minima_de_poblacion": densidad_minima_de_poblacion,
        "altura_maxima_de_edificacion_contino_pareado": altura_maxima_de_edificacion_contino_pareado,
        "altura_maxima_de_edificacion_aislado": altura_maxima_de_edificacion_aislado,
        "sistema_de_agrupamiento": sistema_de_agrupamiento,
        "coeficiente_de_constructibilidad": coeficiente_de_constructibilidad,
        "coeficiente_de_ocupacion_de_suelo": coeficiente_de_ocupacion_de_suelo,
        "ocupacion_pisos_superiores": ocupacion_pisos_superiores,
        "rasante": rasante,
        "nivel_de_aplicacion": nivel_de_aplicacion,
        "adosamientos": adosamientos,
        "distanciamiento": distanciamiento,
        "cierros_hacia_espacio_publico_3_3_8_prr_altura": cierros_hacia_espacio_publico_3_3_8_prr_altura,
        "cierros_hacia_espacio_publico_3_3_8_prr_transparencia": cierros_hacia_espacio_publico_3_3_8_prr_transparencia,
        "cierros_hacia_espacio_publico_3_3_9_prr_altura_minima": cierros_hacia_espacio_publico_3_3_9_prr_altura_minima,
        "cierros_hacia_espacio_publico_3_3_9_prr_altura_maxima": cierros_hacia_espacio_publico_3_3_9_prr_altura_maxima,
        "ochavos": ochavos,
        "antejardin": antejardin,
        "normas_urbanisticas_especiales": normas_urbanisticas_especiales,
        "exigencias_estacionamiento": exigencias_estacionamiento,
        "area_de_riesgo": area_de_riesgo,
        "area_de_proteccion": area_de_proteccion,
        "zona_o_inmueble_conservacion_historica": zona_o_inmueble_conservacion_historica,
        "zona_tipica_o_monumento_nacional": zona_tipica_o_monumento_nacional,
    }


    por_calle = "AV. EINSTEIN SUR"
    tipo_de_via_condicion = "TRONCAL T76N – EXISTENTE"
    distnacia_entre_lineas_oficiales = "20,00m."
    antejardin = "3,00m."

    lineas_oficiales = {
        "por_calle": por_calle,
        "tipo_de_via_condicion": tipo_de_via_condicion,
        "distnacia_entre_lineas_oficiales": distnacia_entre_lineas_oficiales,
        "antejardin": antejardin,
    }

    afectacion_utilidad_publica = {
        "propiedad_afecta_a_declaratoria_de_utilidad_publica": False,
    }

    caracteristicas_de_la_urbanizacion = {
        "urbanizacion_ejecutada": True
    }

    pago_de_derechos = {
        "total_pagado": "$13.020",
        "giro_ingreso_municipal": "30437487",
        "fecha_de_pago": "26.07.2023",
    }


    state_update = {
        "identificacion_propiedad": identificacion_propiedad,
        "instrumentos_aplicables": instrumentos_aplicables,
        "debe_acompanar_informe_calidad_subsuelo": debe_acompanar_informe_calidad_subsuelo,
        "usos_de_suelo": usos_de_suelo,
        "lineas_oficiales": lineas_oficiales,
        "afectacion_utilidad_publica": afectacion_utilidad_publica,
        "caracteristicas_de_la_urbanizacion": caracteristicas_de_la_urbanizacion,
        "pago_de_derechos": pago_de_derechos,
    }
    return Command(
        update={"cip_data": state_update}
    )