require 'date'
require 'uri'
require 'net/http'
require 'json'

def get_data
  puts 'Calculadora de inversión de fintual'

  puts 'Ingrese fecha de la inversión en formato DD/MM/YYYY:'
  while date = gets.chomp
    valid_format = date.match(%r{(?<day>\d{2})/(?<month>\d{2})/(?<year>\d{4})})
    valid_date = begin
                   Date.strptime(date, '%d/%m/%Y')
                 rescue StandardError
                   false
                 end
    if valid_format && valid_date && valid_date < Date.today
      break
    else
      puts 'Se debe ingresar fecha de la inversión en formato DD/MM/YYYY y debe ser una fecha anterior a hoy:'
    end
  end

  puts 'Ingrese monto a invertir en pesos:'
  while amount = gets.chomp.delete('.').delete('$')
    if (begin
         amount = Integer(amount)
       rescue StandardError
         false
       end) && amount > 0
      break
    else
      puts 'Se debe ingresar monto a invertir en pesos:'
    end
  end

  puts 'Ingrese la distribución de su portafolio:'
  while true
    portfolio = {
      "risky_norris": 0,
      "moderate_pitt": 0,
      "conservative_clooney": 0
    }
    if gets.chomp == '{'
      while (aux = gets.chomp) != '}'
        if data = aux.match(/(?<key>risky_norris|moderate_pitt|conservative_clooney)\s*:\s*(?<value>[0-1].[0-9])\s*,/)
          portfolio[data['key'].to_sym] = Float(data['value'])
        else
          break
        end
      end

      break if (portfolio.values.inject(:+) - 1).abs < 0.01
    end
    puts 'Asegrúrese que los valores sumen 1 e ingrese la distribución de la siguiente forma:'
    puts '{'
    puts 'Contenido'
    puts '}'
  end
  {"date": valid_date.strftime("%Y-%m-%d"), "amount": amount, "portfolio": portfolio}
end

def fintual_calculator
  data = get_data 
  puts buying_price = get_stock_price(data[:date], "risky_norris")
end

def get_stock_price(date,fund)
  fund_ids = {
      "risky_norris": 186,
      "moderate_pitt": 187,
      "conservative_clooney": 188
  }
  id = fund_ids[fund.to_sym]
  uri = URI("https://fintual.cl/api/real_assets/#{id}/days?date=#{date}")
  res = Net::HTTP.get_response(uri)
  json = JSON.parse(res.body) if res.is_a?(Net::HTTPSuccess)

  if json["data"][0]
    json["data"][0]["attributes"]["price"]
  else
    false
  end
end

fintual_calculator()