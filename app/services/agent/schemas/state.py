from typing_extensions import TypedDict, Annotated, Literal
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages

class IdentificacionPropiedad(TypedDict):
    cip_id: str
    cip_numero: str
    cip_fecha: str
    calle: str
    loteo: str
    manzana: str
    lote: str
    rol: str
    numero_asignado: str

class InstrumentosAplicables(TypedDict):
    plan_intercomunal_o_metropolitano: str
    plan_regulador_comunal: str
    mod_1_plano_regulador_comunal: str
    mod_2_plano_regulador_comunal: str
    area_de_ubicacion: Literal["Urbana", "Extension Urbana", "Rural"]

class DeclaratoriaPostergacionPermiso(TypedDict, total=False):
    plazo_vigencia: str
    decreto_o_resolucion: str
    fecha: str

class UsosDeSuelo(TypedDict, total=False):
    zona_emplazamiento: str
    usos_permitidos: str
    usos_prohibidos: str
    zona_o_subzona_edificacion_emplazamiento: str
    superficie_de_subdivision_predial_minima: str
    densidad_maxima_de_poblacion: str
    densidad_minima_de_poblacion: str
    altura_maxima_de_edificacion_contino_pareado: str
    altura_maxima_de_edificacion_aislado: str
    sistema_de_agrupamiento: str
    coeficiente_de_constructibilidad: str
    coeficiente_de_ocupacion_de_suelo: str
    ocupacion_pisos_superiores: str
    rasante: str
    nivel_de_aplicacion: str
    adosamientos: str
    distanciamiento: str
    cierros_hacia_espacio_publico_3_3_8_prr_altura: str
    cierros_hacia_espacio_publico_3_3_8_prr_transparencia: str
    cierros_hacia_espacio_publico_3_3_9_prr_altura_minima: str
    cierros_hacia_espacio_publico_3_3_9_prr_altura_maxima: str
    ochavos: str
    antejardin: str
    normas_urbanisticas_especiales: str
    cesiones_areas_verdes: str
    exigencias_estacionamiento: str
    area_de_riesgo: bool
    area_de_proteccion: bool
    zona_o_inmueble_conservacion_historica: bool
    zona_tipica_o_monumento_nacional: bool

class LineasOficiales(TypedDict, total=False):
    por_calle: str
    tipo_de_via_condicion: str
    distnacia_entre_lineas_oficiales: str
    antejardin: str
    distancia_entre_lineas_oficiales_y_eje_calzada: str
    calzada: str


class ObrasDeUrbanizacionDeAreasAfectasADeclaratoria(TypedDict, total=False):
    pavimentacion: bool
    agua_potable: bool
    alcantarillado_aguas_servidas: bool
    evacuacion_de_aguas_pluviales: bool
    electricidad_y_alumbrado_publico: bool
    gas: bool
    telecomunicaciones: bool
    plantacion_y_obras_de_ornato: bool
    obras_de_defensa_del_terreno: bool
    otros: bool
    
class AfectacionUtilidadPublica(TypedDict, total=False):
    propiedad_afecta_a_declaratoria_de_utilidad_publica: bool
    parque: bool
    vialidad: bool
    ensanche: bool
    apertura: bool
    de_las_siguientes_vias: str
    distancia_a_la_vias: str
    orientacion_del_area_afectada: str
    perfil_del_area_afecta_a_obligacion_de_urbanizacion: str
    obras_de_urbanizacion_de_areas_afectas_a_declaratoria: ObrasDeUrbanizacionDeAreasAfectasADeclaratoria

class CaracteristicasDeLaUrbanizacion(TypedDict, total=False):
    urbanizacion_ejecutada: bool
    urbanizacion_recibida: bool
    urbanizacion_garantizada: bool


class DocumentosAdjuntos(TypedDict, total=False):
    planos_de_catastro: bool
    perfiles_de_calles: bool
    anexo_normas_urbanisticas: bool

class PagoDeDerechos(TypedDict, total=False):
    total_pagado: str
    giro_ingreso_municipal: str
    fecha_de_pago: str

class CipData(TypedDict, total=False):
    identificacion_propiedad: IdentificacionPropiedad
    instrumentos_aplicables: InstrumentosAplicables
    declaratoria_postergacion_permiso: DeclaratoriaPostergacionPermiso
    debe_acompanar_informe_calidad_subsuelo: bool
    usos_de_suelo: UsosDeSuelo
    lineas_oficiales: LineasOficiales
    afectacion_utilidad_publica: AfectacionUtilidadPublica
    caracteristicas_de_la_urbanizacion: CaracteristicasDeLaUrbanizacion
    documentos_adjuntos: DocumentosAdjuntos
    pago_de_derechos: PagoDeDerechos


class ProjectState(TypedDict, total=False):
    project_name: str
    project_description: str
    project_status: str
    project_owner: str
    project_created_at: str
    project_updated_at: str
    cip_data: CipData
    messages: Annotated[list[AnyMessage], add_messages]
    item_acta_observaciones: Literal["Uso de Suelo", "Coeficiente de Constructibilidad", "Estacionamientos"]
    resolucion_item: Literal["Cumple", "No Cumple", "No aplica"]