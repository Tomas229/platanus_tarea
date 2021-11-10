require 'date'

def fintual_calculator()
  puts "Calculadora de inversión de fintual"

  puts "Ingrese fecha de la inversión en formato DD/MM/YYYY:"
  while date = gets.chomp
    valid_format = date.match(/(?<day>\d{2})\/(?<month>\d{2})\/(?<year>\d{4})/)
    valid_date = Date.strptime(date,"%d/%m/%Y") rescue false
    if (valid_format && valid_date)
      break
    else 
      puts "Se debe ingresar fecha de la inversión en formato DD/MM/YYYY:"
    end 
  end

  puts "Ingrese monto a invertir en pesos:"
  while amount = gets.chomp.delete('.').delete('$')
    if (Integer(amount) rescue false)  
      break
    else 
      puts "Se debe ingresar monto a invertir en pesos:"
    end 
  end

  puts "Ingrese la distribución de su portafolio:"
  while true
    portfolio = {
      "risky_norris": 0,
      "moderate_pitt": 0,
      "conservative_clooney": 0,
    }
    if (gets.chomp == "{")
      while((aux = gets.chomp) != "}")
        if data = aux.match(/(?<key>risky_norris|moderate_pitt|conservative_clooney)\s*:\s*(?<value>[0-1].[0-9])\s*,/)
          portfolio[data["key"].to_sym] = Float(data["value"])
        else
          break
        end 
      end

      if (portfolio.values.inject(:+) - 1).abs < 0.01
        break
      end
    end
    puts "Asegrúrese que los valores sumen 1 e ingrese la distribución de la siguiente forma:"
    puts "{"
    puts "Contenido"
    puts "}"
  end
  puts date, amount, portfolio
end

fintual_calculator()