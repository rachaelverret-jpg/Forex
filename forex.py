from forex_python.converter import CurrencyRates , CurrencyCodes

c = CurrencyRates()
print(c.get_rates('', ''))

curr=CurrencyCodes()

print(curr.get_symbol(currency_code))

print(curr.get_currency_name(currency_code))

@forex.route("/")
def show_form():

@forex.route("/convert")
def handle_form():

    code_from = request.args['code_from'].upper()
    code_to = request.args['code_to'].upper()
    amt = safe_convert_to_float(request.args['amt'])
    errs = []

    if amt is None:
        return None
    if not currency.check(CurrencyCodes)
    this.showmessage: "this isn not a valed currency"

    else:
        return render_template("forex.html"), results=f"{results}"
