# encoding: UTF-8
#!usr/bin/env ruby

require 'webrick'

include WEBrick

$server = HTTPServer.new(:Port => 8081, :DocumentRoot => "~/document_root")

trap("INT"){ $server.shutdown }
$server.start
