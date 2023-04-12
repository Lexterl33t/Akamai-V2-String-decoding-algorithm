def step2(logical_operation)
  if logical_operation <= 65535
    return logical_operation.chr
  end
end

def decode_string(cipher_string, key)
  first_step = ""
  array_chelou = [466, 59]

  i = cipher_string.length-1
  while (i >= 0)
    valid_index_for_key = ( ( ( (i + -213) - array_chelou[array_chelou.length - 1] ) + 290 ) % key.length)

    last_byte_cipher = cipher_string[i].ord
    key_byte = key[valid_index_for_key].ord

    puts last_byte_cipher

    logical_operation = (( ~last_byte_cipher | ~key_byte ) & ( last_byte_cipher | key_byte ))

    first_step+= step2(logical_operation)
    i-=1
  end

  puts first_step
end


cipher = "%mg\f\x1B\v\"\nq\\0\t\x15?\\r\x18\r\x1EA\x18\f\x13wC\b"
puts cipher[7]
key = "2T]|_A+u!"
decode_string(cipher, key)
