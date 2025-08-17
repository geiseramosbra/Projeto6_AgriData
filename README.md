# Projeto 6 — AgriData Impact Analysis

Análise de impacto de insumos e clima na produtividade agrícola na América Latina (dados sintéticos prontos + guia para migrar para dados reais do World Bank).

## Estrutura
```
AgriData-Impact-Analysis/
├─ data/
│  ├─ raw/                       # coloque aqui os dados reais (World Bank etc.)
│  ├─ processed/                 # dados tratados (gerados pelo notebook)
│  ├─ exports/                   # CSVs prontos para Power BI/Tableau
│  └─ synthetic/                 # dataset sintético (pronto para começar)
├─ docs/
│  ├─ KPIs.md
│  └─ data_dictionary.md
├─ notebooks/
│  └─ Projeto6_AgriData_Impact_Analysis.ipynb
├─ src/                          # utilitários (opcional)
└─ dashboards/
   ├─ powerbi/
   └─ tableau/
```

## Como começar (Windows • PowerShell)
> **Dica:** copie e cole os comandos abaixo no PowerShell.

1) **Criar e ativar ambiente virtual (opcional porém recomendado)**
```powershell
cd "$env:USERPROFILE\Downloads\AgriData-Impact-Analysis"
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
py -m pip install -U pip
py -m pip install jupyter pandas numpy matplotlib scikit-learn pyarrow
```

2) **Abrir o notebook**
```powershell
py -m jupyter notebook ".\notebooks\Projeto6_AgriData_Impact_Analysis.ipynb"
```

## Usando dados reais (World Bank)
- Baixe os indicadores em CSV pelo DataBank/Downloads e salve em:
  `data/raw/worldbank_indicators_latam.csv`
- Reabra/rode o notebook. Ele detecta automaticamente este arquivo e faz o pipeline.

### Indicadores sugeridos (nomes comuns)
- Produtividade / produção agrícola (yield)
- Consumo de fertilizantes (kg/ha)
- Precipitação / chuva (mm) e temperatura média anual (°C)
- Irrigação (% área irrigada)
- Valor agregado da agricultura (US$) / % do PIB
- Emprego na agricultura (% emprego total)
- População rural (% da população)
- Emissões relacionadas à agricultura (Mt CO₂e)
- Inflação de alimentos (% a.a.)

> Observação: nomes/códigos variam; use o buscador do World Bank para encontrar o indicador equivalente para cada país latino-americano e período.

## Saídas prontas
- `data/exports/kpi_yield_5y_by_country.csv`
- `data/exports/kpi_water_productivity_5y_by_country.csv`
- `data/exports/kpi_emissions_intensity_5y_by_country.csv`
- `data/exports/kpi_employment_shift_since_2010.csv`

## Licença
Uso educacional. Dataset sintético criado para prática.