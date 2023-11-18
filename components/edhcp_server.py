#pesudo code for EDHCP server


#receive and parse DHCPDiscover message
  #authenticate the client
  #check for available IP addresses

#send DHCPOffer message
   #add the client to the list of waiting-clients
   #send DHCPOffer message with available IP address


#receive and parse DHCPRequest message
    #check if the client is in the list of waiting-clients
    #check if the IP address is available
    #check if the IP address is the same as the one offered
    #check if the client is authenticated

#send DHCPAck message





 