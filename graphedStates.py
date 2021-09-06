import pandas as pd
from datetime import datetime
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.models import LinearAxis, Range1d, HoverTool, CustomJS
from bokeh.models.widgets import CheckboxGroup
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

#import info from .csv and store in data frame
file = "us-states.csv"
df = pd.read_csv(file)

#Figure graph
graphs = figure(title = "Use Chechboxes on the Right to Select States", x_axis_label='DATE', y_axis_label='CONFIRMED CASES OF COVID-19', x_axis_type='datetime',y_range=(0,60000),tools='pan,box_zoom,zoom_in,zoom_out,reset,save',plot_width=1000, plot_height=500)
graphs.extra_y_ranges = {"foo": Range1d(start=0, end=6000)}
graphs.add_layout(LinearAxis(y_range_name="foo", axis_label='DEATHS FROM COVID-19'), 'right')


#group all info by state then graph conf and dead for each state  
count = 0
plots_Conf = []
plots_Dead = []
places = []
w = 0

for i in sorted(df['state'].unique()):
    #print(w,i)
    places.append(i)
    w = w + 1
    
alabama = "Alabama"
alabamaDates = []
alabamaConf = []
alabamaDead = []

alaska = "Alaska"
alaskaDates = []
alaskaConf = []
alaskaDead = []

arizona = "Arizona"
arizonaDates = []
arizonaConf = []
arizonaDead = []

arkansas = "Arkansas"
arkansasDates = []
arkansasConf = []
arkansasDead = []

california = "California"
californiaDates = []
californiaConf = []
californiaDead = []

colorado = "Colorado"
coloradoDates = []
coloradoConf = []
coloradoDead = []

connecticut = "Connecticut"
connecticutDates = []
connecticutConf = []
connecticutDead = []

delaware = "Delaware"
delawareDates = []
delawareConf = []
delawareDead = []

DoC = "District of Columbia"
DoCDates = []
DoCConf = []
DoCDead = []

florida = "Florida"
floridaDates = []
floridaConf = []
floridaDead = []

georgia = "Georgia"
georgiaDates = []
georgiaConf = []
georgiaDead = []

guam = "Guam"
guamDates = []
guamConf = []
guamDead = []

hawaii = "Hawaii"
hawaiiDates = []
hawaiiConf = []
hawaiiDead = []

idaho = "Idaho"
idahoDates = []
idahoConf = []
idahoDead = []

illinois = "Illinois"
illinoisDates = []
illinoisConf = []
illinoisDead = []

indiana = "Indiana"
indianaDates = []
indianaConf = []
indianaDead = []

iowa = "Iowa"
iowaDates = []
iowaConf = []
iowaDead = []

kansas = "Kansas"
kansasDates = []
kansasConf = []
kansasDead = []

kentucky = "Kentucky"
kentuckyDates = []
kentuckyConf = []
kentuckyDead = []

louisiana = "Louisiana"
louisianaDates = []
louisianaConf = []
louisianaDead = []

maine = "Maine"
maineDates = []
maineConf = []
maineDead = []

maryland = "Maryland"
marylandDates = []
marylandConf = []
marylandDead = []

massachusetts = "Massachusetts"
massachusettsDates = []
massachusettsConf = []
massachusettsDead = []

michigan = "Michigan"
michiganDates = []
michiganConf = []
michiganDead = []

minnesota = "Minnesota"
minnesotaDates = []
minnesotaConf = []
minnesotaDead = []

mississippi = "Mississippi"
mississippiDates = []
mississippiConf = []
mississippiDead = []

missouri = "Missouri"
missouriDates = []
missouriConf = []
missouriDead = []

montana = "Montana"
montanaDates = []
montanaConf = []
montanaDead = []

nebraska = "Nebraska"
nebraskaDates = []
nebraskaConf = []
nebraskaDead = []

nevada = "Nevada"
nevadaDates = []
nevadaConf = []
nevadaDead = []

NH = "New Hampshire"
NHDates = []
NHConf = []
NHDead = []

NJ = "New Jersey"
NJDates = []
NJConf = []
NJDead = []

NM = "New Mexico"
NMDates = []
NMConf = []
NMDead = []

NY = "New York"
NYDates = []
NYConf = []
NYDead = []

NC = "North Carolina"
NCDates = []
NCConf = []
NCDead = []

ND = "North Dakota"
NDDates = []
NDConf = []
NDDead = []

NMI = "Northern Mariana Islands"
NMIDates = []
NMIConf = []
NMIDead = []

ohio = "Ohio"
ohioDates = []
ohioConf = []
ohioDead = []

oklahoma = "Oklahoma"
oklahomaDates = []
oklahomaConf = []
oklahomaDead = []

oregon = "Oregon"
oregonDates = []
oregonConf = []
oregonDead = []

pennsylvania = "Pennsylvania"
pennsylvaniaDates = []
pennsylvaniaConf = []
pennsylvaniaDead = []

PR = "Puerto Rico"
PRDates = []
PRConf = []
PRDead = []

RI = "Rhode Island"
RIDates = []
RIConf = []
RIDead = []

SC = "South Carolina"
SCDates = []
SCConf = []
SCDead = []

SD = "South Dakota"
SDDates = []
SDConf = []
SDDead = []

tennessee = "Tennessee"
tennesseeDates = []
tennesseeConf = []
tennesseeDead = []

texas = "Texas"
texasDates = []
texasConf = []
texasDead = []

utah = "Utah"
utahDates = []
utahConf = []
utahDead = []

vermont = "Vermont"
vermontDates = []
vermontConf = []
vermontDead = []

VI = "Virgin Islands"
VIDates = []
VIConf = []
VIDead = []

virginia = "Virginia"
virginiaDates = []
virginiaConf = []
virginiaDead = []

washington = "Washington"
washingtonDates = []
washingtonConf = []
washingtonDead = []

WV = "West Virginia"
WVDates = []
WVConf = []
WVDead = []

wisconsin = "Wisconsin"
wisconsinDates = []
wisconsinConf = []
wisconsinDead = []

wyoming = "Wyoming"
wyomingDates = []
wyomingConf = []
wyomingDead = []

for place in df['state']:
    if(place == alabama):
        alabamaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        alabamaConf.append(df.iloc[count]['cases'])
        alabamaDead.append(df.iloc[count]['deaths'])
    elif(place == alaska):
        alaskaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        alaskaConf.append(df.iloc[count]['cases'])
        alaskaDead.append(df.iloc[count]['deaths'])
    elif(place == arizona):
        arizonaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        arizonaConf.append(df.iloc[count]['cases'])
        arizonaDead.append(df.iloc[count]['deaths'])
    elif(place == arkansas):
        arkansasDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        arkansasConf.append(df.iloc[count]['cases'])
        arkansasDead.append(df.iloc[count]['deaths'])
    elif(place == california):
        californiaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        californiaConf.append(df.iloc[count]['cases'])
        californiaDead.append(df.iloc[count]['deaths'])
    elif(place == colorado):
        coloradoDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        coloradoConf.append(df.iloc[count]['cases'])
        coloradoDead.append(df.iloc[count]['deaths'])
    elif(place == connecticut):
        connecticutDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        connecticutConf.append(df.iloc[count]['cases'])
        connecticutDead.append(df.iloc[count]['deaths'])
    elif(place == delaware):
        delawareDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        delawareConf.append(df.iloc[count]['cases'])
        delawareDead.append(df.iloc[count]['deaths'])
    elif(place == DoC):
        DoCDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        DoCConf.append(df.iloc[count]['cases'])
        DoCDead.append(df.iloc[count]['deaths'])
    elif(place == florida):
        floridaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        floridaConf.append(df.iloc[count]['cases'])
        floridaDead.append(df.iloc[count]['deaths'])
    elif(place == georgia):
        georgiaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        georgiaConf.append(df.iloc[count]['cases'])
        georgiaDead.append(df.iloc[count]['deaths'])
    elif(place == guam):
        guamDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        guamConf.append(df.iloc[count]['cases'])
        guamDead.append(df.iloc[count]['deaths'])
    elif(place == hawaii):
        hawaiiDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        hawaiiConf.append(df.iloc[count]['cases'])
        hawaiiDead.append(df.iloc[count]['deaths'])
    elif(place == idaho):
        idahoDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        idahoConf.append(df.iloc[count]['cases'])
        idahoDead.append(df.iloc[count]['deaths'])
    elif(place == illinois):
        illinoisDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        illinoisConf.append(df.iloc[count]['cases'])
        illinoisDead.append(df.iloc[count]['deaths'])
    elif(place == indiana):
        indianaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        indianaConf.append(df.iloc[count]['cases'])
        indianaDead.append(df.iloc[count]['deaths'])
    elif(place == iowa):
        iowaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        iowaConf.append(df.iloc[count]['cases'])
        iowaDead.append(df.iloc[count]['deaths'])
    elif(place == kansas):
        kansasDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        kansasConf.append(df.iloc[count]['cases'])
        kansasDead.append(df.iloc[count]['deaths'])
    elif(place == kentucky):
        kentuckyDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        kentuckyConf.append(df.iloc[count]['cases'])
        kentuckyDead.append(df.iloc[count]['deaths'])
    elif(place == louisiana):
        louisianaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        louisianaConf.append(df.iloc[count]['cases'])
        louisianaDead.append(df.iloc[count]['deaths'])
    elif(place == maine):
        maineDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        maineConf.append(df.iloc[count]['cases'])
        maineDead.append(df.iloc[count]['deaths'])
    elif(place == maryland):
        marylandDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        marylandConf.append(df.iloc[count]['cases'])
        marylandDead.append(df.iloc[count]['deaths'])
    elif(place == massachusetts):
        massachusettsDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        massachusettsConf.append(df.iloc[count]['cases'])
        massachusettsDead.append(df.iloc[count]['deaths'])
    elif(place == michigan):
        michiganDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        michiganConf.append(df.iloc[count]['cases'])
        michiganDead.append(df.iloc[count]['deaths'])
    elif(place == minnesota):
        minnesotaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        minnesotaConf.append(df.iloc[count]['cases'])
        minnesotaDead.append(df.iloc[count]['deaths'])
    elif(place == mississippi):
        mississippiDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        mississippiConf.append(df.iloc[count]['cases'])
        mississippiDead.append(df.iloc[count]['deaths'])
    elif(place == missouri):
        missouriDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        missouriConf.append(df.iloc[count]['cases'])
        missouriDead.append(df.iloc[count]['deaths'])
    elif(place == montana):
        montanaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        montanaConf.append(df.iloc[count]['cases'])
        montanaDead.append(df.iloc[count]['deaths'])
    elif(place == nebraska):
        nebraskaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        nebraskaConf.append(df.iloc[count]['cases'])
        nebraskaDead.append(df.iloc[count]['deaths'])
    elif(place == nevada):
        nevadaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        nevadaConf.append(df.iloc[count]['cases'])
        nevadaDead.append(df.iloc[count]['deaths'])
    elif(place == NH):
        NHDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        NHConf.append(df.iloc[count]['cases'])
        NHDead.append(df.iloc[count]['deaths'])
    elif(place == NJ):
        NJDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        NJConf.append(df.iloc[count]['cases'])
        NJDead.append(df.iloc[count]['deaths'])
    elif(place == NM):
        NMDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        NMConf.append(df.iloc[count]['cases'])
        NMDead.append(df.iloc[count]['deaths'])
    elif(place == NY):
        NYDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        NYConf.append(df.iloc[count]['cases'])
        NYDead.append(df.iloc[count]['deaths'])
    elif(place == NC):
        NCDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        NCConf.append(df.iloc[count]['cases'])
        NCDead.append(df.iloc[count]['deaths'])
    elif(place == ND):
        NDDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        NDConf.append(df.iloc[count]['cases'])
        NDDead.append(df.iloc[count]['deaths'])
    elif(place == NMI):
        NMIDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        NMIConf.append(df.iloc[count]['cases'])
        NMIDead.append(df.iloc[count]['deaths'])
    elif(place == ohio):
        ohioDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        ohioConf.append(df.iloc[count]['cases'])
        ohioDead.append(df.iloc[count]['deaths'])
    elif(place == oklahoma):
        oklahomaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        oklahomaConf.append(df.iloc[count]['cases'])
        oklahomaDead.append(df.iloc[count]['deaths'])
    elif(place == oregon):
        oregonDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        oregonConf.append(df.iloc[count]['cases'])
        oregonDead.append(df.iloc[count]['deaths'])
    elif(place == pennsylvania):
        pennsylvaniaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        pennsylvaniaConf.append(df.iloc[count]['cases'])
        pennsylvaniaDead.append(df.iloc[count]['deaths'])
    elif(place == PR):
        PRDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        PRConf.append(df.iloc[count]['cases'])
        PRDead.append(df.iloc[count]['deaths'])
    elif(place == RI):
        RIDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        RIConf.append(df.iloc[count]['cases'])
        RIDead.append(df.iloc[count]['deaths'])
    elif(place == SC):
        SCDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        SCConf.append(df.iloc[count]['cases'])
        SCDead.append(df.iloc[count]['deaths'])
    elif(place == SD):
        SDDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        SDConf.append(df.iloc[count]['cases'])
        SDDead.append(df.iloc[count]['deaths'])
    elif(place == tennessee):
        tennesseeDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        tennesseeConf.append(df.iloc[count]['cases'])
        tennesseeDead.append(df.iloc[count]['deaths'])
    elif(place == texas):
        texasDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        texasConf.append(df.iloc[count]['cases'])
        texasDead.append(df.iloc[count]['deaths'])
    elif(place == utah):
        utahDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        utahConf.append(df.iloc[count]['cases'])
        utahDead.append(df.iloc[count]['deaths'])
    elif(place == vermont):
        vermontDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        vermontConf.append(df.iloc[count]['cases'])
        vermontDead.append(df.iloc[count]['deaths'])
    elif(place == VI):
        VIDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        VIConf.append(df.iloc[count]['cases'])
        VIDead.append(df.iloc[count]['deaths'])
    elif(place == virginia):
        virginiaDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        virginiaConf.append(df.iloc[count]['cases'])
        virginiaDead.append(df.iloc[count]['deaths'])
    elif(place == washington):
        washingtonDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        washingtonConf.append(df.iloc[count]['cases'])
        washingtonDead.append(df.iloc[count]['deaths'])
    elif(place == WV):
        WVDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        WVConf.append(df.iloc[count]['cases'])
        WVDead.append(df.iloc[count]['deaths'])
    elif(place == wisconsin):
        wisconsinDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        wisconsinConf.append(df.iloc[count]['cases'])
        wisconsinDead.append(df.iloc[count]['deaths'])
    elif(place == wyoming):
        wyomingDates.append(datetime.strptime(df.iloc[count]['date'], '%Y-%m-%d'))
        wyomingConf.append(df.iloc[count]['cases'])
        wyomingDead.append(df.iloc[count]['deaths'])
        

    count = count + 1
    
plots_Conf.append(graphs.line(alabamaDates,alabamaConf,line_width=2,line_color='black',name=alabama,legend_label="Confirmed"))
plots_Dead.append(graphs.line(alabamaDates,alabamaDead,line_width=2,line_dash='dashed',line_color='black',name=alabama, y_range_name="foo",legend_label="Deaths"))

plots_Conf.append(graphs.line(alaskaDates,alaskaConf,line_width=2,line_color='blue',name=alaska,visible=False))
plots_Dead.append(graphs.line(alaskaDates,alaskaDead,line_width=2,line_dash='dashed',line_color='blue',name=alaska, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(arizonaDates,arizonaConf,line_width=2,line_color='brown',name=arizona,visible=False))
plots_Dead.append(graphs.line(arizonaDates,arizonaDead,line_width=2,line_dash='dashed',line_color='brown',name=arizona, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(arkansasDates,arkansasConf,line_width=2,line_color='cadetblue',name=arkansas,visible=False))
plots_Dead.append(graphs.line(arkansasDates,arkansasDead,line_width=2,line_dash='dashed',line_color='cadetblue',name=arkansas, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(californiaDates,californiaConf,line_width=2,line_color='coral',name=california,visible=False))
plots_Dead.append(graphs.line(californiaDates,californiaDead,line_width=2,line_dash='dashed',line_color='coral',name=california, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(coloradoDates,coloradoConf,line_width=2,line_color='crimson',name=colorado,visible=False))
plots_Dead.append(graphs.line(coloradoDates,coloradoDead,line_width=2,line_dash='dashed',line_color='crimson',name=colorado, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(connecticutDates,connecticutConf,line_width=2,line_color='darkblue',name=connecticut,visible=False))
plots_Dead.append(graphs.line(connecticutDates,connecticutDead,line_width=2,line_dash='dashed',line_color='darkblue',name=connecticut, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(delawareDates,delawareConf,line_width=2,line_color='darkgoldenrod',name=delaware,visible=False))
plots_Dead.append(graphs.line(delawareDates,delawareDead,line_width=2,line_dash='dashed',line_color='darkgoldenrod',name=delaware, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(DoCDates,DoCConf,line_width=2,line_color='darkgreen',name=DoC,visible=False))
plots_Dead.append(graphs.line(DoCDates,DoCDead,line_width=2,line_dash='dashed',line_color='darkgreen',name=DoC, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(floridaDates,floridaConf,line_width=2,line_color='darkkhaki',name=florida,visible=False))
plots_Dead.append(graphs.line(floridaDates,floridaDead,line_width=2,line_dash='dashed',line_color='darkkhaki',name=florida, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(georgiaDates,georgiaConf,line_width=2,line_color='darkolivegreen',name=georgia,visible=False))
plots_Dead.append(graphs.line(georgiaDates,georgiaDead,line_width=2,line_dash='dashed',line_color='darkolivegreen',name=georgia, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(guamDates,guamConf,line_width=2,line_color='darkorchid',name=guam,visible=False))
plots_Dead.append(graphs.line(guamDates,guamDead,line_width=2,line_dash='dashed',line_color='darkorchid',name=guam, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(hawaiiDates,hawaiiConf,line_width=2,line_color='darksalmon',name=hawaii,visible=False))
plots_Dead.append(graphs.line(hawaiiDates,hawaiiDead,line_width=2,line_dash='dashed',line_color='darksalmon',name=hawaii, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(idahoDates,idahoConf,line_width=2,line_color='darkslateblue',name=idaho,visible=False))
plots_Dead.append(graphs.line(idahoDates,idahoDead,line_width=2,line_dash='dashed',line_color='darkslateblue',name=idaho, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(illinoisDates,illinoisConf,line_width=2,line_color='darkslategrey',name=illinois,visible=False))
plots_Dead.append(graphs.line(illinoisDates,illinoisDead,line_width=2,line_dash='dashed',line_color='darkslategrey',name=illinois, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(indianaDates,indianaConf,line_width=2,line_color='darkviolet',name=indiana,visible=False))
plots_Dead.append(graphs.line(indianaDates,indianaDead,line_width=2,line_dash='dashed',line_color='darkviolet',name=indiana, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(iowaDates,iowaConf,line_width=2,line_color='deepskyblue',name=iowa,visible=False))
plots_Dead.append(graphs.line(iowaDates,iowaDead,line_width=2,line_dash='dashed',line_color='deepskyblue',name=iowa, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(kansasDates,kansasConf,line_width=2,line_color='dimgrey',name=kansas,visible=False))
plots_Dead.append(graphs.line(kansasDates,kansasDead,line_width=2,line_dash='dashed',line_color='dimgrey',name=kansas, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(kentuckyDates,kentuckyConf,line_width=2,line_color='firebrick',name=kentucky,visible=False))
plots_Dead.append(graphs.line(kentuckyDates,kentuckyDead,line_width=2,line_dash='dashed',line_color='firebrick',name=kentucky, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(louisianaDates,louisianaConf,line_width=2,line_color='fuchsia',name=louisiana,visible=False))
plots_Dead.append(graphs.line(louisianaDates,louisianaDead,line_width=2,line_dash='dashed',line_color='fuchsia',name=louisiana, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(maineDates,maineConf,line_width=2,line_color='goldenrod',name=maine,visible=False))
plots_Dead.append(graphs.line(maineDates,maineDead,line_width=2,line_dash='dashed',line_color='goldenrod',name=maine, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(marylandDates,marylandConf,line_width=2,line_color='green',name=maryland,visible=False))
plots_Dead.append(graphs.line(marylandDates,marylandDead,line_width=2,line_dash='dashed',line_color='green',name=maryland, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(massachusettsDates,massachusettsConf,line_width=2,line_color='grey',name=massachusetts,visible=False))
plots_Dead.append(graphs.line(massachusettsDates,massachusettsDead,line_width=2,line_dash='dashed',line_color='grey',name=massachusetts, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(michiganDates,michiganConf,line_width=2,line_color='indianred',name=michigan,visible=False))
plots_Dead.append(graphs.line(michiganDates,michiganDead,line_width=2,line_dash='dashed',line_color='indianred',name=michigan, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(minnesotaDates,minnesotaConf,line_width=2,line_color='indigo',name=minnesota,visible=False))
plots_Dead.append(graphs.line(minnesotaDates,minnesotaDead,line_width=2,line_dash='dashed',line_color='indigo',name=minnesota, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(mississippiDates,mississippiConf,line_width=2,line_color='indigo',name=mississippi,visible=False))
plots_Dead.append(graphs.line(mississippiDates,mississippiDead,line_width=2,line_dash='dashed',line_color='indigo',name=mississippi, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(missouriDates,missouriConf,line_width=2,line_color='lawngreen',name=missouri,visible=False))
plots_Dead.append(graphs.line(missouriDates,missouriDead,line_width=2,line_dash='dashed',line_color='lawngreen',name=missouri, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(montanaDates,montanaConf,line_width=2,line_color='lightblue',name=montana,visible=False))
plots_Dead.append(graphs.line(montanaDates,montanaDead,line_width=2,line_dash='dashed',line_color='lightblue',name=montana, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(nebraskaDates,nebraskaConf,line_width=2,line_color='lightcoral',name=nebraska,visible=False))
plots_Dead.append(graphs.line(nebraskaDates,nebraskaDead,line_width=2,line_dash='dashed',line_color='lightcoral',name=nebraska, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(nevadaDates,nevadaConf,line_width=2,line_color='lightgreen',name=nevada,visible=False))
plots_Dead.append(graphs.line(nevadaDates,nevadaDead,line_width=2,line_dash='dashed',line_color='lightgreen',name=nevada, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(NHDates,NHConf,line_width=2,line_color='lightpink',name=NH,visible=False))
plots_Dead.append(graphs.line(NHDates,NHDead,line_width=2,line_dash='dashed',line_color='lightpink',name=NH, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(NJDates,NJConf,line_width=2,line_color='lightsalmon',name=NJ,visible=False))
plots_Dead.append(graphs.line(NJDates,NJDead,line_width=2,line_dash='dashed',line_color='lightsalmon',name=NJ, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(NMDates,NMConf,line_width=2,line_color='lime',name=NM,visible=False))
plots_Dead.append(graphs.line(NMDates,NMDead,line_width=2,line_dash='dashed',line_color='lime',name=NM, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(NYDates,NYConf,line_width=2,line_color='magenta',name=NY,visible=False))
plots_Dead.append(graphs.line(NYDates,NYDead,line_width=2,line_dash='dashed',line_color='magenta',name=NY, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(NCDates,NCConf,line_width=2,line_color='mediumaquamarine',name=NC,visible=False))
plots_Dead.append(graphs.line(NCDates,NCDead,line_width=2,line_dash='dashed',line_color='mediumaquamarine',name=NC, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(NDDates,NDConf,line_width=2,line_color='mediumpurple',name=ND,visible=False))
plots_Dead.append(graphs.line(NDDates,NDDead,line_width=2,line_dash='dashed',line_color='mediumpurple',name=ND, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(NMIDates,NMIConf,line_width=2,line_color='mediumslateblue',name=NMI,visible=False))
plots_Dead.append(graphs.line(NMIDates,NMIDead,line_width=2,line_dash='dashed',line_color='mediumslateblue',name=NMI, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(ohioDates,ohioConf,line_width=2,line_color='mediumspringgreen',name=ohio,visible=False))
plots_Dead.append(graphs.line(ohioDates,ohioDead,line_width=2,line_dash='dashed',line_color='mediumspringgreen',name=ohio, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(oklahomaDates,oklahomaConf,line_width=2,line_color='mediumturquoise',name=oklahoma,visible=False))
plots_Dead.append(graphs.line(oklahomaDates,oklahomaDead,line_width=2,line_dash='dashed',line_color='mediumturquoise',name=oklahoma, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(oregonDates,oregonConf,line_width=2,line_color='mediumvioletred',name=oregon,visible=False))
plots_Dead.append(graphs.line(oregonDates,oregonDead,line_width=2,line_dash='dashed',line_color='mediumvioletred',name=oregon, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(pennsylvaniaDates,pennsylvaniaConf,line_width=2,line_color='midnightblue',name=pennsylvania,visible=False))
plots_Dead.append(graphs.line(pennsylvaniaDates,pennsylvaniaDead,line_width=2,line_dash='dashed',line_color='midnightblue',name=pennsylvania, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(PRDates,PRConf,line_width=2,line_color='navy',name=PR,visible=False))
plots_Dead.append(graphs.line(PRDates,PRDead,line_width=2,line_dash='dashed',line_color='navy',name=PR, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(RIDates,RIConf,line_width=2,line_color='olive',name=RI,visible=False))
plots_Dead.append(graphs.line(RIDates,RIDead,line_width=2,line_dash='dashed',line_color='olive',name=RI, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(SCDates,SCConf,line_width=2,line_color='orange',name=SC,visible=False))
plots_Dead.append(graphs.line(SCDates,SCDead,line_width=2,line_dash='dashed',line_color='orange',name=SC, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(SDDates,SDConf,line_width=2,line_color='orangered',name=SD,visible=False))
plots_Dead.append(graphs.line(SDDates,SDDead,line_width=2,line_dash='dashed',line_color='orangered',name=SD, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(tennesseeDates,tennesseeConf,line_width=2,line_color='palegreen',name=tennessee,visible=False))
plots_Dead.append(graphs.line(tennesseeDates,tennesseeDead,line_width=2,line_dash='dashed',line_color='palegreen',name=tennessee, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(texasDates,texasConf,line_width=2,line_color='peru',name=texas,visible=False))
plots_Dead.append(graphs.line(texasDates,texasDead,line_width=2,line_dash='dashed',line_color='peru',name=texas, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(utahDates,utahConf,line_width=2,line_color='pink',name=utah,visible=False))
plots_Dead.append(graphs.line(utahDates,utahDead,line_width=2,line_dash='dashed',line_color='pink',name=utah, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(vermontDates,vermontConf,line_width=2,line_color='powderblue',name=vermont,visible=False))
plots_Dead.append(graphs.line(vermontDates,vermontDead,line_width=2,line_dash='dashed',line_color='powderblue',name=vermont, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(VIDates,VIConf,line_width=2,line_color='purple',name=VI,visible=False))
plots_Dead.append(graphs.line(VIDates,VIDead,line_width=2,line_dash='dashed',line_color='purple',name=VI, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(virginiaDates,virginiaConf,line_width=2,line_color='red',name=virginia,visible=False))
plots_Dead.append(graphs.line(virginiaDates,virginiaDead,line_width=2,line_dash='dashed',line_color='red',name=virginia, y_range_name="foo",visible=False))
    
plots_Conf.append(graphs.line(washingtonDates,washingtonConf,line_width=2,line_color='powderblue',name=washington,visible=False))
plots_Dead.append(graphs.line(washingtonDates,washingtonDead,line_width=2,line_dash='dashed',line_color='powderblue',name=washington, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(WVDates,WVConf,line_width=2,line_color='skyblue',name=WV,visible=False))
plots_Dead.append(graphs.line(WVDates,WVDead,line_width=2,line_dash='dashed',line_color='skyblue',name=WV, y_range_name="foo",visible=False))

plots_Conf.append(graphs.line(wisconsinDates,wisconsinConf,line_width=2,line_color='turquoise',name=wisconsin,visible=False))
plots_Dead.append(graphs.line(wisconsinDates,wisconsinDead,line_width=2,line_dash='dashed',line_color='turquoise',name=wisconsin, y_range_name="foo",visible=False))
 
plots_Conf.append(graphs.line(wyomingDates,wyomingConf,line_width=2,line_color='violet',name=wyoming,visible=False))
plots_Dead.append(graphs.line(wyomingDates,wyomingDead,line_width=2,line_dash='dashed',line_color='violet',name=wyoming, y_range_name="foo",visible=False))

graphs.sizing_mode = 'scale_both'
graphs.legend.location = 'top_left'
graphs.left[0].formatter.use_scientific = False
graphs.right[0].formatter.use_scientific = False
graphs.add_tools(HoverTool(tooltips=[("", "$name"),("","$x{%F}: $y{int}")],formatters = {"$x": "datetime"},mode='mouse',toggleable=False)) 

checkboxes = CheckboxGroup(labels=places, active=[0])


#Linking with JavaScript
callback = CustomJS(code="""
                            var i;
                            for (i = 0; i < 55; i++)
                            {
                                if (cb_obj.active.includes(i))
                                {
                                    lineC[i].visible = true;
                                    lineD[i].visible = true;
                                }
                                else
                                {
                                    lineC[i].visible = false;
                                    lineD[i].visible = false;
                                }
                            }
                            """,
                    args={'lineC': plots_Conf, 'lineD': plots_Dead})


checkboxes.js_on_click(callback)
print("niice, graph 42 location: stateGraphs.txt")
output_file("USstates.html")
show(row(graphs,checkboxes))
#html = file_html(row(graphs,checkboxes), CDN, "US States")
#fa = open("stateGraphs.txt","w")
#fa.write(html)
