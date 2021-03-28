def teater31 (title, ticket_sales, price_per_ticket, *city) :
    total_income = ticket_sales * price_per_ticket
    return f"Tiket film {title} terjual sebanyak {ticket_sales} dengan total pendapatan Rp.{total_income}, diputar di kota {city}"

print(teater31("Spider Man", 100, 5000, "Jakarta", "Surabaya"))
print(teater31("Iron Man", 300, 10000, "Jakarta", "Surabaya", "Malang"))