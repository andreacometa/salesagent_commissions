<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body>

	<h1 class="centered">RIEPILOGO PROVVIGIONI</h1>

	<table class="table_data">
		<tr>
			<td colspan="3"></td>
			<td colspan="2">PROVV.</td>
			<td colspan="2">PAGAMENTO</td>
			<td colspan="3">FATTURA</td>
		</tr>
		<tr>
			<td class="centered">AGENTE</td>
			<td class="centered">DESCRIZIONE</td>
			<td class="centered">SUBTOTALE</td>
			<td class="centered">%</td>
			<td class="centered">TOTALE</td>
			<td class="centered">DATA</td>
			<td class="centered">NOTE</td>
			<td class="centered">FATTURA</td>
			<td class="centered">DATA FATTURA</td>
			<td class="centered">CLIENTE</td>
		</tr>
	% for record in objects:
		<tr>
			<td>${record.salesagent_id.name}</td>
			<td>${record.name}</td>
			<td>${record.price_subtotal}</td>
			<td>${record.commission_percentage}</td>
			<td>${record.commission}</td>
			<td>${record.payment_commission_date or ''}</td>
			<td>${record.payment_commission_note or ''}</td>
			<td>${record.invoice_id.number or ''}</td>
			<td>${record.date_invoice or ''}</td>
			<td>${record.partner_id.name or ''}</td>
		</tr>
	%endfor
	</table>

</body>
</html>
