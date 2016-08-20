---
title: "Desempleo Masculino vs Femenino"
author: "Patricio del Boca"
date: "August 20, 2016"
output: html_document
layout: post
---

Revisando el nuevo Portal de [Gobierno Abierto de la Ciudad de Córdoba](https://gobiernoabierto.cordoba.gov.ar/) me encontré un Data Set con [Indicadores del mercado laboral](https://gobiernoabierto.cordoba.gov.ar/data/datos-abiertos/categoria/mercado-laboral/indicadores-del-mercado-laboral-aglomerado-gran-cordoba-2007-a-2015/54).


Charlando con la gente de [Open Data Córdoba](opendatacordoba.org) siempre salen temas relacionados con la igualdad de género y cómo transparentar, a través del uso de datos abiertos, la situación de ambos géneros en la ciudad. Ya sea en el ámbito deportivo, cultural, profesional, laboral. Por ende me interesó graficar la evolución de la Tasa de Desempleo de Mujeres, con respecto a la Tasa de Desempleo de Hombres.

#### Análisis
El conjunto de datos no estaba en un formato que pueda ser utilizado directamente para el análisis, por lo fue requerido una primera limpieza manual con [LibreOffice Calc](https://es.libreoffice.org/descubre/calc/).


{% highlight r %}
df <- read.csv('../data/desempleo-masculino-vs-femenino/mercado_laboral.csv')

difPromedio <- ave(df$Tasa.de.desocupacion.de.mujeres - df$Tasa.de.desocupacion.de.varones)

ggplot(df, aes(Trimestre)) +
 geom_line(aes(y=Tasa.de.desocupacion.de.mujeres,
               colour="Tasa.de.desocupacion.de.mujeres", group=1)) +
 geom_line(aes(y=Tasa.de.desocupacion.de.varones,
               colour="Tasa.de.desocupacion.de.varones", group=1)) +
  theme_fivethirtyeight() +
  theme(
    axis.text.x = element_text(angle = 30, hjust = 1.1),
    legend.title = element_blank()) +
  labs(
    title="Tasa de Desocupación por Género",
    subtitle=paste0("Tasa de desocupación por género en la Ciudad de Córdoba del 2007 al 2015. Diferencia Promedio: ", round(difPromedio,2),"%"),
    caption="Open Data Córdoba - Fuente: https://gobiernoabierto.cordoba.gov.ar/"
  )
{% endhighlight %}

<img src="/figs/2016-08-20-Desempleo-masculino-vs-femenino/plot-1.png" title="center" alt="center" style="display: block; margin: auto;" />

#### Conclusión:
La diferencia promedio entre la Tasa de Desocupación de Mujeres y la Tasa de Desocupación de Varones entre el 2007 y el 2015 es de **3.32%**.