# This script is for Jenkins using role based strategy plugin. 

require 'net/http'
require 'uri'

user=ENV['JENKINS_ADMIN']
password=ENV['JENKINS_ADMIN_PASSWORD']
type=ENV['TYPE']
roleName=ENV['ROLE_NAME']
sid=ENV['SID']
jenkins=ENV['JENKINS']

puts type
puts roleName
puts sid
puts jenkins


uri = URI.parse("http://#{jenkins}/jenkins/role-strategy/strategy/assignRole")
request = Net::HTTP::Post.new(uri)
request.basic_auth(user, password)
request.set_form_data(
  "type" => type,
  "roleName" => roleName,
  "sid" => sid,
)

response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https") do |http|
  http.request(request)
end

puts response
