import pandas as pd
import matplotlib.pyplot as plt

try: 
    df = pd.read_csv('finanzas2020[1].csv', sep = '\t')
except Exception as error:
    print('No se ha podido leer el fichero ', error)
    raise SystemExit

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
for a, b in zip(df.columns, meses):
    if(a.lower()!=b.lower()):
        raise SystemExit ("Error: Las columnas son incorrectas.")
for col in df.columns:
    if(df[col].empty):
        print("Columna vacía.")
        df[col].drop([col], axis=1)

for col in df.columns:
    df[col] = df[col].apply(lambda x: x.replace("'", "") if type(x)==str else x)
    try:
        df[col] = df[col].astype(float)
    except Exception as e:
        print("Error en columna",col,':',e)
        for val in df[col].values:
            try:
                float(val)
            except:
                df[col] = df[col].apply(lambda x: 0 if x==val else x)
    df[col] = df[col].astype(float)


calculos_df = pd.DataFrame(index=df.columns, columns=['ingresos', 'gastos', 'ahorros'])

for col in df.columns:
    gastos = 0
    ahorros = 0 
    ingresos = 0


    for val in df[col].values:
        if(val < 0):
            gastos = gastos + val
        else:
            ingresos = ingresos + val
        ahorros = ahorros + val
    calculos_df.loc[col] = [ingresos, gastos, ahorros]
    # calculos_df.append({'Mes': col, 'ingresos': ingresos, 'gastos': gastos, 'ahorros': ahorros}, ignore_index=True)
print('')
print('Mes que se ha gastado más: ', calculos_df[calculos_df['gastos']==calculos_df['gastos'].min(axis=0)].index[0])
print('Mes que se ha ahorrado más: ', calculos_df[calculos_df['ahorros']==calculos_df['ahorros'].max(axis=0)].index[0])
print('Media de gastos al año: ', calculos_df['gastos'].mean())
print('Gasto total a lo largo del año: ', calculos_df['gastos'].sum())

calculos_df['ingresos'].plot()

plt.legend()
plt.title("Ingresos a lo largo del año")
plt.xlabel('Date')
plt.ylabel('Ingresos')
plt.savefig('ingresos.png')
plt.show()



