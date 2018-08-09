# encoding: UTF-8
#!usr/bin/env ruby

require 'webrick'

include WEBrick

$server = HTTPServer.new(:Port => 8081, :DocumentRoot => "~/document_root")

load ("./httpserver_servlet_handler.rb")

trap("INT"){ $server.shutdown }
$server.start
