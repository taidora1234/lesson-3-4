{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install yfinance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "crude_oil_ticker = \"CL=F\"\n",
    "exr_eurusd_ticker = \"EURUSD=X\"\n",
    "hist = crude_oil.history()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = yf.download(crude_oil_ticker)\n",
    "exr = yf.download(exr_eurusd_ticker)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Затраты на производство\n",
    "PRODUCTION_COST = 400 # (EUR)\n",
    "\n",
    "# Расходы на логистику\n",
    "EU_LOGISTIC_COST_EUR = 30 # в Европу в евро\n",
    "CN_LOGISTIC_COST_USD = 130 # в Китай в долларах\n",
    "\n",
    "# * Справочная информация по клиентам(объемы, локации, комментарии) \n",
    "customers = {\n",
    "    'Сonty':{\n",
    "        'location':'EU',\n",
    "        'volumes':200,\n",
    "        'comment':'moving_average'\n",
    "    },\n",
    "    \n",
    "    'Triangle':{\n",
    "        'location':'CN',\n",
    "        'volumes': 30,\n",
    "        'comment': 'monthly'\n",
    "    },\n",
    "    'Stone':{\n",
    "        'location':'EU',\n",
    "        'volumes': 150,\n",
    "        'comment': 'moving_average'\n",
    "    },\n",
    "    'Ant':{\n",
    "        'location':'EU',\n",
    "        'volumes': 70,\n",
    "        'comment': 'monthly'\n",
    "    }\n",
    "}\n",
    "# Скидки\n",
    "discounts = {'99': 0.01, # до 100 тонн 1%\n",
    "             '299': 0.05, #  до 300 тонн 5%\n",
    "             '300': 0.1}   # больше 300 тонн 10%\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "year = '2023'\n",
    "month = '03'\n",
    "\n",
    "grade = url = f\"https://www.lgm.gov.my/webv2api/api/rubberprice/month={month}&year={year}\"\n",
    "res = requests.get(url)\n",
    "rj = res.json()\n",
    "df2 = pd.json_normalize(rj)\n",
    "df2.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df2['us'] = pd.to_numeric(df2['us'], errors='coerce')\n",
    "df2.dropna(inplace=True)\n",
    "df2['trunc'] = pd.to_datetime(df2['date']).dt.to_period('M')\n",
    "df2 = df2[df2['grade']=='SMR 10']\n",
    "result = df2.groupby('trunc')['us'].mean()\n",
    "df_now = result.to_frame(name='average_us') * 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.concat([data.resample('M').mean()['Close'], exr.resample('M').mean()['Close']], axis=1)\n",
    "df.columns = ['crude_oil_price', 'eureusd']\n",
    "df = df['2022-01-01':'2022-12-31']\n",
    "# # Formula (10*Data + 400 ) * Discount + Logistics\n",
    "df[\"proccessing_usd\"] = df['eureusd'] * 400\n",
    "df[\"base_wpb_price_usd\"] = df[\"crude_oil_price\"]*10 + df['proccessing_usd']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_volume_discounts(x):\n",
    "  if 0 < x <= 99:\n",
    "    return 0.01\n",
    "  elif 99 < x <= 299:\n",
    "    return 0.05\n",
    "  elif x >= 300:\n",
    "    return 0.1\n",
    "  else:\n",
    "    return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def price_now(x,y,z,w):\n",
    "    new = x * (1-y) + z\n",
    "    if new > w:\n",
    "        return new\n",
    "    else: \n",
    "        return w"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'os' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/1k/rp772snj2y55b6h_cpgh3prh0000gn/T/ipykernel_59741/3872132418.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mclients_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'for_clients'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmakedirs\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mclients_path\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexist_ok\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mclient_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclient_info\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcustomers\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0mclient_df\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'os' is not defined"
     ]
    }
   ],
   "source": [
    "clients_path = 'for_clients'\n",
    "os.makedirs(clients_path, exist_ok=True)\n",
    "\n",
    "for client_name, client_info in customers.items():\n",
    "    client_df = df.copy()\n",
    "    \n",
    "    if client_info.get('location') == 'EU':\n",
    "      client_df['logistics'] = client_df['eureusd'] * EU_LOGISTIC_COST_EUR\n",
    "    elif client_info.get('location') == 'CN':\n",
    "      client_df['logistics'] = CN_LOGISTIC_COST_USD\n",
    "    \n",
    "    if client_info.get('volumes'):\n",
    "      client_df['volumes'] = client_info.get('volumes')\n",
    "\n",
    "    client_df['discount'] = client_df['volumes'].apply(check_volume_discounts)\n",
    "    average_us = df_now['average_us'][0]\n",
    "    client_df['WBP_price_usd'] = client_df.apply(lambda x: price_now(x['base_wpb_price_usd'],x['discount'],x['logistics'],average_us), axis=1)\n",
    "    \n",
    "    client_df['WBP_price_usd'].plot(color='red', linestyle=\"dashed\")\n",
    "    plt.title(f\"Client {client_name} WBP Price\")\n",
    "    plt.ylabel(\"USD\")\n",
    "    plt.tight_layout()\n",
    "    plt.savefig(f'{client_name}_wbp_price.png')\n",
    "    plt.close()\n",
    "\n",
    "    client_df = client_df.round(2)\n",
    "    client_df = client_df.reset_index()\n",
    "    client_df.Date = client_df.Date.dt.strftime('%B %Y')\n",
    "    \n",
    "    max_row, max_col = client_df.shape\n",
    "    xlfilepath = os.path.join(clients_path, f'{client_name}_wbp_prices.xlsx')\n",
    "    with pd.ExcelWriter(xlfilepath, engine='xlsxwriter') as writer:\n",
    "        client_df.to_excel(writer, sheet_name=client_name, startrow=1, header=False, index=False)\n",
    "        workbook = writer.book\n",
    "        worksheet = writer.sheets[client_name]\n",
    "        column_settings = [{'header': column} for column in client_df.columns]\n",
    "        worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})\n",
    "        worksheet.insert_image(max_row + 3, 1, f'{client_name}_wbp_price.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
