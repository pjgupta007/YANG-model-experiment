from ncclient import manager
import device_info
import xmltodict
import xml.dom.minidom

"""
   This is a template to create route-map 
   using YANG data model driven programmability
"""

route_map = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <route-map>
        <name>RM-IN</name>
        <route-map-without-order-seq xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-route-map">
          <seq_no>10</seq_no>
          <operation>permit</operation>
          <match>
            <ip>
              <address>
                <prefix-list>PL-IN</prefix-list>
              </address>
            </ip>
          </match>
        </route-map-without-order-seq>
      </route-map>
      <route-map>
        <name>RM-OUT</name>
        <route-map-without-order-seq xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-route-map">
          <seq_no>10</seq_no>
          <operation>permit</operation>
          <match>
            <ip>
              <address>
                <prefix-list>PL-OUT</prefix-list>
              </address>
            </ip>
          </match>
        </route-map-without-order-seq>
      </route-map>
    </native>
</config>
"""
with manager.connect(host="ios-xe-mgmt.cisco.com",
                     port=10000,
                     username='root',
                     password='D_Vay!_10&',
                     hostkey_verify=False) as m:

   
   



   route_map_config = m.edit_config(target = "running", config = route_map)
   #route_map_xml=xml.dom.minidom.parseString(route_map_config.xml)
   #print(route_map_xml.toprettyxml(indent = "  "))


           
