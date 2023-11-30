import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

product_df = pd.read_csv('products_dataset.csv')
order_item_df = pd.read_csv("order_items_dataset.csv")
order_payment_df = pd.read_csv("order_payments_dataset.csv")



new_join = pd.merge(
    left = product_df[["product_id","product_category_name"]],
    right = order_item_df[["product_id","order_id"]],
    how = "inner",
    left_on = "product_id",
    right_on = "product_id"
)
where1 = new_join.groupby(["product_category_name"])["order_id"].count().sort_values(ascending = True)\
                 .reset_index(name="total_orders")
where2 = new_join.groupby(["product_category_name"])["order_id"].count().sort_values(ascending = False)\
                 .reset_index(name="total_orders")
where3 = order_payment_df.groupby(["payment_type"])["order_id"].count().sort_values(ascending = False)\
                         .reset_index(name="total")



st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader("Produk dengan Jumlah Permintaan Terbanyak dan Tersedikit di E-Commerce Brazil")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(40, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="total_orders", y="product_category_name", data=where2.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing Product", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="total_orders", y="product_category_name", data=where1.sort_values(by="total_orders", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].yaxis.set_label_position("left")
ax[1].yaxis.tick_left()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
st.pyplot(fig)



st.subheader("Jenis - Jenis Metode Pembayaran yang Digunakan di E-Commerce Brazil")

explode = (0.05, 0.05, 0.05, 0.05, 0.05)

where3.groupby(['payment_type']).sum().plot(
    kind='pie', y='total', autopct='%1.2f%%', explode=explode, title = 'Payments Method in Brazilian E-Commerce', legend = False)
plt.show()
st.pyplot()
