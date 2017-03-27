#!/usr/bin/ruby

size = Integer(ARGV[0])
unless ARGV[1].nil?
  inputs = Integer(ARGV[1])
else
  inputs = 1 
end
for i in 0..inputs do 
  start_times = Array.new(size) { rand (1..900) }  
  finish_times = Array.new(size) { |index| rand(start_times[index]+1..1000) }
  output = File.new("inputs/input_#{size}_#{i}.txt", 'w')
  (0..size-1).step(1) do |i|
    output << start_times[i] << ' ' << finish_times[i] << "\n"
  end
end

