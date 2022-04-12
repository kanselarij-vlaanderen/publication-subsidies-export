column_name_map = {
    "opschrift": "Opschrift",
    "trefwoord": "Trefwoord",
    "opdrachtgever": "Opdrachtgever",
    "datum": "datum",
    "opdracht_x0020_formeel_x0020_ontvangen": "Datum formeel ontvangen",
    "aantal_x0020_blz": "Aantal bladzijden",
    "beleidsdomein": "Beleidsdomein",
    "bevoegde_x0020_minister_x0028_s_x0029_": "Bevoegde Ministers",
    "opmerkingen": "Opmerkingen",
    "document_x0020_nr": "Document naam",
    "vloeiboek_x0020_ontvangen": "Datum vloeiboek ontvangen",
    "vloeiboek_x0020_naar_x0020_m-p": "Datum Vloeiboek naar m-p",
    "vloeiboek_x0020_terug_x0020_van_x0020_m-p": "Datum Vloeiboek terug van m-p",
    'verspreiding': "Datum verspreiding"
}

type_map = {
    "datum": "datetime64",
    "opdracht_x0020_formeel_x0020_ontvangen": "datetime64",
    "vloeiboek_x0020_ontvangen": "datetime64",
    "vloeiboek_x0020_naar_x0020_m-p": "datetime64",
    "vloeiboek_x0020_terug_x0020_van_x0020_m-p": "datetime64",
    'verspreiding': "datetime64"
}
import pandas

in_path = "/data/DOSSIEROPVOLGING-H.xml"
out_path = "/data/subsidiedossier_opvolging_1998_2022.csv"

df = pandas.read_xml(in_path, xpath='//Dossieropvolging/dossiernummer[.="0-subsidie"]/..|//Dossieropvolging/dossiernummer[.="0-Subsidie"]/..')

df = df.astype(type_map)
df = df.filter(column_name_map.keys(), axis="columns")
df = df.rename(column_name_map, axis="columns")

df.to_csv(
    out_path,
    sep=';',
    na_rep='',
    header=True,
    index=False,
    mode='w',
    quoting=None,
    quotechar='"',
    line_terminator=None,
    date_format="%d-%m-%Y",
    doublequote=True,
    escapechar=None,
    decimal=',',
    errors='strict')