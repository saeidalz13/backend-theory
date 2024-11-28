def clean_up_session_ids
  Thread.new do
    num = 0
    while true
      puts "loop #{num}"
      num += 1
  
      # some db cleaning task
  
      # Do this loop for every 10 minutes
      sleep 60 * 10
    end
  end
end


clean_up_session_ids


sleep 10
puts "Main thread ended"