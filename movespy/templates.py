# Copyright (c) 2013, Resource Systems Group, Inc.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
#     - Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#     
#     - Redistributions in binary form must reproduce the above copyright notice, 
#       this list of conditions and the following disclaimer in the documentation 
#       and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.

runspec_template = """
<runspec>
	<description><![CDATA[]]></description>
	<modelscale value="Inv"/>
	<modeldomain value="PROJECT"/>
	<geographicselections>
		<geographicselection type="COUNTY" key="" description=""/>
	</geographicselections>
	<timespan>
		<year key=""/>
		<month id=""/>
		<day id=""/>
		<beginhour id=""/>
		<endhour id=""/>
		<aggregateBy key="Hour"/>
	</timespan>
	<onroadvehicleselections>
		<onroadvehicleselection fueltypeid="3" fueltypedesc="Compressed Natural Gas (CNG)" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="62" sourcetypename="Combination Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="61" sourcetypename="Combination Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="41" sourcetypename="Intercity Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="53" sourcetypename="Single Unit Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="61" sourcetypename="Combination Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="11" sourcetypename="Motorcycle"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="53" sourcetypename="Single Unit Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="42" sourcetypename="Transit Bus"/>
	</onroadvehicleselections>
	<offroadvehicleselections>
	</offroadvehicleselections>
	<offroadvehiclesccs>
	</offroadvehiclesccs>
	<roadtypes>
		<roadtype roadtypeid="2" roadtypename="Rural Restricted Access"/>
		<roadtype roadtypeid="3" roadtypename="Rural Unrestricted Access"/>
		<roadtype roadtypeid="4" roadtypename="Urban Restricted Access"/>
		<roadtype roadtypeid="5" roadtypename="Urban Unrestricted Access"/>
	</roadtypes>
	<pollutantprocessassociations>
		<pollutantprocessassociation pollutantkey="132" pollutantname="1,2,3,4,6,7,8-Heptachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="144" pollutantname="1,2,3,4,6,7,8-Heptachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="137" pollutantname="1,2,3,4,7,8,9-Heptachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="134" pollutantname="1,2,3,4,7,8-Hexachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="145" pollutantname="1,2,3,4,7,8-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="141" pollutantname="1,2,3,6,7,8-Hexachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="140" pollutantname="1,2,3,6,7,8-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="130" pollutantname="1,2,3,7,8,9-Hexachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="146" pollutantname="1,2,3,7,8,9-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="135" pollutantname="1,2,3,7,8-Pentachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="139" pollutantname="1,2,3,7,8-Pentachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="24" pollutantname="1,3-Butadiene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="24" pollutantname="1,3-Butadiene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="40" pollutantname="2,2,4-Trimethylpentane" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="40" pollutantname="2,2,4-Trimethylpentane" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="143" pollutantname="2,3,4,6,7,8-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="138" pollutantname="2,3,4,7,8-Pentachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="142" pollutantname="2,3,7,8-Tetrachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="136" pollutantname="2,3,7,8-Tetrachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="170" pollutantname="Acenaphthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="170" pollutantname="Acenaphthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="70" pollutantname="Acenaphthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="70" pollutantname="Acenaphthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="171" pollutantname="Acenaphthylene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="171" pollutantname="Acenaphthylene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="71" pollutantname="Acenaphthylene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="71" pollutantname="Acenaphthylene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="26" pollutantname="Acetaldehyde" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="26" pollutantname="Acetaldehyde" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="27" pollutantname="Acrolein" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="27" pollutantname="Acrolein" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="30" pollutantname="Ammonia (NH3)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="30" pollutantname="Ammonia (NH3)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="172" pollutantname="Anthracene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="172" pollutantname="Anthracene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="72" pollutantname="Anthracene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="72" pollutantname="Anthracene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="63" pollutantname="Arsenic Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="90" pollutantname="Atmospheric CO2" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="173" pollutantname="Benz(a)anthracene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="173" pollutantname="Benz(a)anthracene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="73" pollutantname="Benz(a)anthracene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="73" pollutantname="Benz(a)anthracene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="20" pollutantname="Benzene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="20" pollutantname="Benzene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="174" pollutantname="Benzo(a)pyrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="174" pollutantname="Benzo(a)pyrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="74" pollutantname="Benzo(a)pyrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="74" pollutantname="Benzo(a)pyrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="175" pollutantname="Benzo(b)fluoranthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="175" pollutantname="Benzo(b)fluoranthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="75" pollutantname="Benzo(b)fluoranthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="75" pollutantname="Benzo(b)fluoranthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="176" pollutantname="Benzo(g,h,i)perylene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="176" pollutantname="Benzo(g,h,i)perylene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="76" pollutantname="Benzo(g,h,i)perylene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="76" pollutantname="Benzo(g,h,i)perylene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="177" pollutantname="Benzo(k)fluoranthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="177" pollutantname="Benzo(k)fluoranthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="77" pollutantname="Benzo(k)fluoranthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="77" pollutantname="Benzo(k)fluoranthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="99" pollutantname="Brake Specific Fuel Consumption (BSFC)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="98" pollutantname="CO2 Equivalent" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="2" pollutantname="Carbon Monoxide (CO)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="2" pollutantname="Carbon Monoxide (CO)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="64" pollutantname="Chromium 3+" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="65" pollutantname="Chromium 6+" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="178" pollutantname="Chrysene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="178" pollutantname="Chrysene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="78" pollutantname="Chrysene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="78" pollutantname="Chrysene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="168" pollutantname="Dibenzo(a,h)anthracene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="168" pollutantname="Dibenzo(a,h)anthracene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="68" pollutantname="Dibenzo(a,h)anthracene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="68" pollutantname="Dibenzo(a,h)anthracene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="21" pollutantname="Ethanol" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="21" pollutantname="Ethanol" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="41" pollutantname="Ethyl Benzene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="41" pollutantname="Ethyl Benzene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="169" pollutantname="Fluoranthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="169" pollutantname="Fluoranthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="69" pollutantname="Fluoranthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="69" pollutantname="Fluoranthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="181" pollutantname="Fluorene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="181" pollutantname="Fluorene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="81" pollutantname="Fluorene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="81" pollutantname="Fluorene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="25" pollutantname="Formaldehyde" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="25" pollutantname="Formaldehyde" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="93" pollutantname="Fossil Fuel Energy Consumption" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="42" pollutantname="Hexane" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="42" pollutantname="Hexane" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="182" pollutantname="Indeno(1,2,3,c,d)pyrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="182" pollutantname="Indeno(1,2,3,c,d)pyrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="82" pollutantname="Indeno(1,2,3,c,d)pyrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="82" pollutantname="Indeno(1,2,3,c,d)pyrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="22" pollutantname="MTBE" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="22" pollutantname="MTBE" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="66" pollutantname="Manganese Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="61" pollutantname="Mercury Divalent Gaseous" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="60" pollutantname="Mercury Elemental Gaseous" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="62" pollutantname="Mercury Particulate" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="5" pollutantname="Methane (CH4)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="5" pollutantname="Methane (CH4)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="185" pollutantname="Naphthalene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="185" pollutantname="Naphthalene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="23" pollutantname="Naphthalene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="23" pollutantname="Naphthalene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="67" pollutantname="Nickel Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="33" pollutantname="Nitrogen Dioxide (NO2)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="33" pollutantname="Nitrogen Dioxide (NO2)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="32" pollutantname="Nitrogen Oxide (NO)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="32" pollutantname="Nitrogen Oxide (NO)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="34" pollutantname="Nitrous Acid (HONO)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="34" pollutantname="Nitrous Acid (HONO)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="6" pollutantname="Nitrous Oxide (N2O)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="6" pollutantname="Nitrous Oxide (N2O)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="79" pollutantname="Non-Methane Hydrocarbons" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="79" pollutantname="Non-Methane Hydrocarbons" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="80" pollutantname="Non-Methane Organic Gases" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="80" pollutantname="Non-Methane Organic Gases" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="131" pollutantname="Octachlorodibenzo-p-dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="133" pollutantname="Octachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="3" pollutantname="Oxides of Nitrogen (NOx)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="3" pollutantname="Oxides of Nitrogen (NOx)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="92" pollutantname="Petroleum Energy Consumption" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="183" pollutantname="Phenanthrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="183" pollutantname="Phenanthrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="83" pollutantname="Phenanthrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="83" pollutantname="Phenanthrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="100" pollutantname="Primary Exhaust PM10  - Total" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="100" pollutantname="Primary Exhaust PM10  - Total" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="110" pollutantname="Primary Exhaust PM2.5 - Total" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="110" pollutantname="Primary Exhaust PM2.5 - Total" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="106" pollutantname="Primary PM10 - Brakewear Particulate" processkey="9" processname="Brakewear"/>
		<pollutantprocessassociation pollutantkey="102" pollutantname="Primary PM10 - Elemental Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="102" pollutantname="Primary PM10 - Elemental Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="101" pollutantname="Primary PM10 - Organic Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="101" pollutantname="Primary PM10 - Organic Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="105" pollutantname="Primary PM10 - Sulfate Particulate" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="105" pollutantname="Primary PM10 - Sulfate Particulate" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="107" pollutantname="Primary PM10 - Tirewear Particulate" processkey="10" processname="Tirewear"/>
		<pollutantprocessassociation pollutantkey="116" pollutantname="Primary PM2.5 - Brakewear Particulate" processkey="9" processname="Brakewear"/>
		<pollutantprocessassociation pollutantkey="112" pollutantname="Primary PM2.5 - Elemental Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="112" pollutantname="Primary PM2.5 - Elemental Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="111" pollutantname="Primary PM2.5 - Organic Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="111" pollutantname="Primary PM2.5 - Organic Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="115" pollutantname="Primary PM2.5 - Sulfate Particulate" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="115" pollutantname="Primary PM2.5 - Sulfate Particulate" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="117" pollutantname="Primary PM2.5 - Tirewear Particulate" processkey="10" processname="Tirewear"/>
		<pollutantprocessassociation pollutantkey="43" pollutantname="Propionaldehyde" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="43" pollutantname="Propionaldehyde" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="184" pollutantname="Pyrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="184" pollutantname="Pyrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="84" pollutantname="Pyrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="84" pollutantname="Pyrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="44" pollutantname="Styrene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="44" pollutantname="Styrene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="31" pollutantname="Sulfur Dioxide (SO2)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="31" pollutantname="Sulfur Dioxide (SO2)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="45" pollutantname="Toluene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="45" pollutantname="Toluene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="91" pollutantname="Total Energy Consumption" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="1" pollutantname="Total Gaseous Hydrocarbons" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="1" pollutantname="Total Gaseous Hydrocarbons" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="86" pollutantname="Total Organic Gases" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="86" pollutantname="Total Organic Gases" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="87" pollutantname="Volatile Organic Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="87" pollutantname="Volatile Organic Compounds" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="46" pollutantname="Xylene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="46" pollutantname="Xylene" processkey="15" processname="Crankcase Running Exhaust"/>
	</pollutantprocessassociations>
	<databaseselections>
	</databaseselections>
	<internalcontrolstrategies>
<internalcontrolstrategy classname="gov.epa.otaq.moves.master.implementation.ghg.internalcontrolstrategies.rateofprogress.RateOfProgressStrategy"><![CDATA[
useParameters	No

]]></internalcontrolstrategy>
	</internalcontrolstrategies>
	<inputdatabase servername="" databasename="" description=""/>
	<uncertaintyparameters uncertaintymodeenabled="false" numberofrunspersimulation="0" numberofsimulations="0"/>
	<geographicoutputdetail description="LINK"/>
	<outputemissionsbreakdownselection>
		<modelyear selected="true"/>
		<fueltype selected="true"/>
		<emissionprocess selected="true"/>
		<onroadoffroad selected="true"/>
		<roadtype selected="true"/>
		<sourceusetype selected="true"/>
		<movesvehicletype selected="false"/>
		<onroadscc selected="false"/>
		<offroadscc selected="false"/>
		<estimateuncertainty selected="false" numberOfIterations="2" keepSampledData="false" keepIterations="false"/>
		<sector selected="false"/>
		<engtechid selected="false"/>
		<hpclass selected="false"/>
	</outputemissionsbreakdownselection>
	<outputdatabase servername="localhost" databasename="xxx_output" description=""/>
	<outputtimestep value="Hour"/>
	<outputvmtdata value="true"/>
	<outputsho value="false"/>
	<outputsh value="false"/>
	<outputshp value="false"/>
	<outputshidling value="false"/>
	<outputstarts value="false"/>
	<outputpopulation value="false"/>
	<scaleinputdatabase servername="localhost" databasename="xxx_input" description=""/>
	<pmsize value="0"/>
	<outputfactors>
		<timefactors selected="true" units="Hours"/>
		<distancefactors selected="true" units="Miles"/>
		<massfactors selected="true" units="Grams" energyunits="KiloJoules"/>
	</outputfactors>
	<savedata>

	</savedata>

	<donotexecute>

	</donotexecute>

	<generatordatabase shouldsave="false" servername="" databasename="" description=""/>
		<donotperformfinalaggregation selected="false"/>
	<lookuptableflags scenarioid="" truncateoutput="false" truncateactivity="false"/>
</runspec>


"""




importscript_template = """

<moves>
	<importer mode="project" >
		<filters>
	<geographicselections>
		<geographicselection type="COUNTY" key="" description=""/>
	</geographicselections>
	<timespan>
		<year key=""/>
		<month id=""/>
		<day id=""/>
		<beginhour id=""/>
		<endhour id=""/>
		<aggregateBy key="Hour"/>
	</timespan>
	<onroadvehicleselections>
		<onroadvehicleselection fueltypeid="3" fueltypedesc="Compressed Natural Gas (CNG)" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="62" sourcetypename="Combination Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="61" sourcetypename="Combination Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="41" sourcetypename="Intercity Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="53" sourcetypename="Single Unit Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="9" fueltypedesc="Electricity" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="61" sourcetypename="Combination Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="11" sourcetypename="Motorcycle"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="53" sourcetypename="Single Unit Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="42" sourcetypename="Transit Bus"/>
	</onroadvehicleselections>
	<offroadvehicleselections>
	</offroadvehicleselections>
	<offroadvehiclesccs>
	</offroadvehiclesccs>
	<roadtypes>
		<roadtype roadtypeid="2" roadtypename="Rural Restricted Access"/>
		<roadtype roadtypeid="3" roadtypename="Rural Unrestricted Access"/>
		<roadtype roadtypeid="4" roadtypename="Urban Restricted Access"/>
		<roadtype roadtypeid="5" roadtypename="Urban Unrestricted Access"/>
	</roadtypes>
	<pollutantprocessassociations>
		<pollutantprocessassociation pollutantkey="132" pollutantname="1,2,3,4,6,7,8-Heptachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="144" pollutantname="1,2,3,4,6,7,8-Heptachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="137" pollutantname="1,2,3,4,7,8,9-Heptachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="134" pollutantname="1,2,3,4,7,8-Hexachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="145" pollutantname="1,2,3,4,7,8-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="141" pollutantname="1,2,3,6,7,8-Hexachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="140" pollutantname="1,2,3,6,7,8-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="130" pollutantname="1,2,3,7,8,9-Hexachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="146" pollutantname="1,2,3,7,8,9-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="135" pollutantname="1,2,3,7,8-Pentachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="139" pollutantname="1,2,3,7,8-Pentachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="24" pollutantname="1,3-Butadiene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="24" pollutantname="1,3-Butadiene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="40" pollutantname="2,2,4-Trimethylpentane" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="40" pollutantname="2,2,4-Trimethylpentane" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="143" pollutantname="2,3,4,6,7,8-Hexachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="138" pollutantname="2,3,4,7,8-Pentachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="142" pollutantname="2,3,7,8-Tetrachlorodibenzo-p-Dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="136" pollutantname="2,3,7,8-Tetrachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="170" pollutantname="Acenaphthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="170" pollutantname="Acenaphthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="70" pollutantname="Acenaphthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="70" pollutantname="Acenaphthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="171" pollutantname="Acenaphthylene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="171" pollutantname="Acenaphthylene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="71" pollutantname="Acenaphthylene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="71" pollutantname="Acenaphthylene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="26" pollutantname="Acetaldehyde" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="26" pollutantname="Acetaldehyde" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="27" pollutantname="Acrolein" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="27" pollutantname="Acrolein" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="30" pollutantname="Ammonia (NH3)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="30" pollutantname="Ammonia (NH3)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="172" pollutantname="Anthracene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="172" pollutantname="Anthracene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="72" pollutantname="Anthracene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="72" pollutantname="Anthracene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="63" pollutantname="Arsenic Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="90" pollutantname="Atmospheric CO2" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="173" pollutantname="Benz(a)anthracene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="173" pollutantname="Benz(a)anthracene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="73" pollutantname="Benz(a)anthracene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="73" pollutantname="Benz(a)anthracene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="20" pollutantname="Benzene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="20" pollutantname="Benzene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="174" pollutantname="Benzo(a)pyrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="174" pollutantname="Benzo(a)pyrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="74" pollutantname="Benzo(a)pyrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="74" pollutantname="Benzo(a)pyrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="175" pollutantname="Benzo(b)fluoranthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="175" pollutantname="Benzo(b)fluoranthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="75" pollutantname="Benzo(b)fluoranthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="75" pollutantname="Benzo(b)fluoranthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="176" pollutantname="Benzo(g,h,i)perylene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="176" pollutantname="Benzo(g,h,i)perylene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="76" pollutantname="Benzo(g,h,i)perylene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="76" pollutantname="Benzo(g,h,i)perylene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="177" pollutantname="Benzo(k)fluoranthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="177" pollutantname="Benzo(k)fluoranthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="77" pollutantname="Benzo(k)fluoranthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="77" pollutantname="Benzo(k)fluoranthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="99" pollutantname="Brake Specific Fuel Consumption (BSFC)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="98" pollutantname="CO2 Equivalent" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="2" pollutantname="Carbon Monoxide (CO)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="2" pollutantname="Carbon Monoxide (CO)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="64" pollutantname="Chromium 3+" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="65" pollutantname="Chromium 6+" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="178" pollutantname="Chrysene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="178" pollutantname="Chrysene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="78" pollutantname="Chrysene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="78" pollutantname="Chrysene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="168" pollutantname="Dibenzo(a,h)anthracene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="168" pollutantname="Dibenzo(a,h)anthracene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="68" pollutantname="Dibenzo(a,h)anthracene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="68" pollutantname="Dibenzo(a,h)anthracene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="21" pollutantname="Ethanol" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="21" pollutantname="Ethanol" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="41" pollutantname="Ethyl Benzene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="41" pollutantname="Ethyl Benzene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="169" pollutantname="Fluoranthene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="169" pollutantname="Fluoranthene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="69" pollutantname="Fluoranthene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="69" pollutantname="Fluoranthene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="181" pollutantname="Fluorene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="181" pollutantname="Fluorene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="81" pollutantname="Fluorene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="81" pollutantname="Fluorene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="25" pollutantname="Formaldehyde" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="25" pollutantname="Formaldehyde" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="93" pollutantname="Fossil Fuel Energy Consumption" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="42" pollutantname="Hexane" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="42" pollutantname="Hexane" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="182" pollutantname="Indeno(1,2,3,c,d)pyrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="182" pollutantname="Indeno(1,2,3,c,d)pyrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="82" pollutantname="Indeno(1,2,3,c,d)pyrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="82" pollutantname="Indeno(1,2,3,c,d)pyrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="22" pollutantname="MTBE" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="22" pollutantname="MTBE" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="66" pollutantname="Manganese Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="61" pollutantname="Mercury Divalent Gaseous" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="60" pollutantname="Mercury Elemental Gaseous" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="62" pollutantname="Mercury Particulate" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="5" pollutantname="Methane (CH4)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="5" pollutantname="Methane (CH4)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="185" pollutantname="Naphthalene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="185" pollutantname="Naphthalene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="23" pollutantname="Naphthalene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="23" pollutantname="Naphthalene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="67" pollutantname="Nickel Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="33" pollutantname="Nitrogen Dioxide (NO2)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="33" pollutantname="Nitrogen Dioxide (NO2)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="32" pollutantname="Nitrogen Oxide (NO)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="32" pollutantname="Nitrogen Oxide (NO)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="34" pollutantname="Nitrous Acid (HONO)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="34" pollutantname="Nitrous Acid (HONO)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="6" pollutantname="Nitrous Oxide (N2O)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="6" pollutantname="Nitrous Oxide (N2O)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="79" pollutantname="Non-Methane Hydrocarbons" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="79" pollutantname="Non-Methane Hydrocarbons" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="80" pollutantname="Non-Methane Organic Gases" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="80" pollutantname="Non-Methane Organic Gases" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="131" pollutantname="Octachlorodibenzo-p-dioxin" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="133" pollutantname="Octachlorodibenzofuran" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="3" pollutantname="Oxides of Nitrogen (NOx)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="3" pollutantname="Oxides of Nitrogen (NOx)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="92" pollutantname="Petroleum Energy Consumption" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="183" pollutantname="Phenanthrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="183" pollutantname="Phenanthrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="83" pollutantname="Phenanthrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="83" pollutantname="Phenanthrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="100" pollutantname="Primary Exhaust PM10  - Total" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="100" pollutantname="Primary Exhaust PM10  - Total" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="110" pollutantname="Primary Exhaust PM2.5 - Total" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="110" pollutantname="Primary Exhaust PM2.5 - Total" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="106" pollutantname="Primary PM10 - Brakewear Particulate" processkey="9" processname="Brakewear"/>
		<pollutantprocessassociation pollutantkey="102" pollutantname="Primary PM10 - Elemental Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="102" pollutantname="Primary PM10 - Elemental Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="101" pollutantname="Primary PM10 - Organic Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="101" pollutantname="Primary PM10 - Organic Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="105" pollutantname="Primary PM10 - Sulfate Particulate" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="105" pollutantname="Primary PM10 - Sulfate Particulate" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="107" pollutantname="Primary PM10 - Tirewear Particulate" processkey="10" processname="Tirewear"/>
		<pollutantprocessassociation pollutantkey="116" pollutantname="Primary PM2.5 - Brakewear Particulate" processkey="9" processname="Brakewear"/>
		<pollutantprocessassociation pollutantkey="112" pollutantname="Primary PM2.5 - Elemental Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="112" pollutantname="Primary PM2.5 - Elemental Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="111" pollutantname="Primary PM2.5 - Organic Carbon" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="111" pollutantname="Primary PM2.5 - Organic Carbon" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="115" pollutantname="Primary PM2.5 - Sulfate Particulate" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="115" pollutantname="Primary PM2.5 - Sulfate Particulate" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="117" pollutantname="Primary PM2.5 - Tirewear Particulate" processkey="10" processname="Tirewear"/>
		<pollutantprocessassociation pollutantkey="43" pollutantname="Propionaldehyde" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="43" pollutantname="Propionaldehyde" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="184" pollutantname="Pyrene gas" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="184" pollutantname="Pyrene gas" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="84" pollutantname="Pyrene particle" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="84" pollutantname="Pyrene particle" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="44" pollutantname="Styrene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="44" pollutantname="Styrene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="31" pollutantname="Sulfur Dioxide (SO2)" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="31" pollutantname="Sulfur Dioxide (SO2)" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="45" pollutantname="Toluene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="45" pollutantname="Toluene" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="91" pollutantname="Total Energy Consumption" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="1" pollutantname="Total Gaseous Hydrocarbons" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="1" pollutantname="Total Gaseous Hydrocarbons" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="86" pollutantname="Total Organic Gases" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="86" pollutantname="Total Organic Gases" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="87" pollutantname="Volatile Organic Compounds" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="87" pollutantname="Volatile Organic Compounds" processkey="15" processname="Crankcase Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="46" pollutantname="Xylene" processkey="1" processname="Running Exhaust"/>
		<pollutantprocessassociation pollutantkey="46" pollutantname="Xylene" processkey="15" processname="Crankcase Running Exhaust"/>
	</pollutantprocessassociations>
		</filters>
		<databaseselection servername="localhost" databasename="xxx_input"/>
		<link>
			<description><![CDATA[]]></description>
			<parts>
				<link>
					<filename></filename>
				</link>
			</parts>
		</link>

		<linksourcetypehour>
			<description><![CDATA[]]></description>
			<parts>
				<linkSourceTypeHour>
					<filename></filename>
				</linkSourceTypeHour>
			</parts>
		</linksourcetypehour>

		<driveschedulesecondlink>
			<description><![CDATA[]]></description>
			<parts>
				<driveScheduleSecondLink>
					<filename></filename>
				</driveScheduleSecondLink>
			</parts>
		</driveschedulesecondlink>

		<offnetworklink>
			<description><![CDATA[]]></description>
			<parts>
				<offNetworkLink>
					<filename></filename>
				</offNetworkLink>
			</parts>
		</offnetworklink>

		<linkopmodedistribution>
			<description><![CDATA[]]></description>
			<parts>
				<opModeDistribution>
					<filename></filename>
				</opModeDistribution>
			</parts>
		</linkopmodedistribution>

		<agedistribution>
			<description><![CDATA[]]></description>
			<parts>
				<sourceTypeAgeDistribution>
					<filename></filename>
				</sourceTypeAgeDistribution>
			</parts>
		</agedistribution>

		<avft>
			<description><![CDATA[]]></description>
			<parts>
				<avft>
					<filename></filename>
				</avft>
			</parts>
		</avft>

		<fuel>
			<description><![CDATA[]]></description>
			<parts>
				<FuelSupply>
					<filename></filename>
				</FuelSupply>
				<FuelFormulation>
					<filename></filename>
				</FuelFormulation>
			</parts>
		</fuel>

		<zonemonthhour>
			<description><![CDATA[]]></description>
			<parts>
				<zoneMonthHour>
					<filename></filename>
				</zoneMonthHour>
			</parts>
		</zonemonthhour>

		<imcoverage>
			<description><![CDATA[]]></description>
			<parts>
				<IMCoverage>
					<filename></filename>
				</IMCoverage>
			</parts>
		</imcoverage>

		<generic>
			<description><![CDATA[]]></description>
			<parts>
				<anytable>
					<tablename>agecategory</tablename>
					<filename></filename>
				</anytable>
			</parts>
		</generic>

	</importer>
</moves>

"""


mean_age_run_spec = """
<runspec>
	<description><![CDATA[]]></description>
	<modelscale value="Inv"/>
	<modeldomain value="NATIONAL"/>
	<geographicselections>
		<geographicselection type="NATION" key="0" description=""/>
	</geographicselections>
	<timespan>
		<year key="2041"/>
		<month id="1"/>
		<month id="2"/>
		<month id="3"/>
		<month id="4"/>
		<month id="5"/>
		<month id="6"/>
		<month id="7"/>
		<month id="8"/>
		<month id="9"/>
		<month id="10"/>
		<month id="11"/>
		<month id="12"/>
		<day id="2"/>
		<day id="5"/>
		<beginhour id="1"/>
		<endhour id="24"/>
		<aggregateBy key="Year"/>
	</timespan>
	<onroadvehicleselections>
		<onroadvehicleselection fueltypeid="3" fueltypedesc="Compressed Natural Gas (CNG)" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="62" sourcetypename="Combination Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="61" sourcetypename="Combination Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="41" sourcetypename="Intercity Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="11" sourcetypename="Motorcycle"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="53" sourcetypename="Single Unit Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="2" fueltypedesc="Diesel Fuel" sourcetypeid="42" sourcetypename="Transit Bus"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="62" sourcetypename="Combination Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="61" sourcetypename="Combination Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="41" sourcetypename="Intercity Bus"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="32" sourcetypename="Light Commercial Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="54" sourcetypename="Motor Home"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="11" sourcetypename="Motorcycle"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="21" sourcetypename="Passenger Car"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="31" sourcetypename="Passenger Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="51" sourcetypename="Refuse Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="43" sourcetypename="School Bus"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="53" sourcetypename="Single Unit Long-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="52" sourcetypename="Single Unit Short-haul Truck"/>
		<onroadvehicleselection fueltypeid="1" fueltypedesc="Gasoline" sourcetypeid="42" sourcetypename="Transit Bus"/>
	</onroadvehicleselections>
	<offroadvehicleselections>
	</offroadvehicleselections>
	<offroadvehiclesccs>
	</offroadvehiclesccs>
	<roadtypes>
		<roadtype roadtypeid="5" roadtypename="Urban Unrestricted Access"/>
	</roadtypes>
	<pollutantprocessassociations>
		<pollutantprocessassociation pollutantkey="2" pollutantname="Carbon Monoxide (CO)" processkey="1" processname="Running Exhaust"/>
	</pollutantprocessassociations>
	<databaseselections>
	</databaseselections>
	<internalcontrolstrategies>
<internalcontrolstrategy classname="gov.epa.otaq.moves.master.implementation.ghg.internalcontrolstrategies.rateofprogress.RateOfProgressStrategy"><![CDATA[
useParameters	No

]]></internalcontrolstrategy>
	</internalcontrolstrategies>
	<inputdatabase servername="" databasename="" description=""/>
	<uncertaintyparameters uncertaintymodeenabled="false" numberofrunspersimulation="0" numberofsimulations="0"/>
	<geographicoutputdetail description="NATION"/>
	<outputemissionsbreakdownselection>
		<modelyear selected="true"/>
		<fueltype selected="true"/>
		<emissionprocess selected="true"/>
		<onroadoffroad selected="true"/>
		<roadtype selected="true"/>
		<sourceusetype selected="true"/>
		<movesvehicletype selected="false"/>
		<onroadscc selected="false"/>
		<offroadscc selected="false"/>
		<estimateuncertainty selected="false" numberOfIterations="2" keepSampledData="false" keepIterations="false"/>
		<sector selected="false"/>
		<engtechid selected="false"/>
		<hpclass selected="false"/>
	</outputemissionsbreakdownselection>
	<outputdatabase servername=" " databasename="" description=""/>
	<outputtimestep value="Year"/>
	<outputvmtdata value="false"/>
	<outputsho value="false"/>
	<outputsh value="false"/>
	<outputshp value="false"/>
	<outputshidling value="false"/>
	<outputstarts value="false"/>
	<outputpopulation value="false"/>
	<scaleinputdatabase servername="" databasename="" description=""/>
	<pmsize value="0"/>
	<outputfactors>
		<timefactors selected="true" units="Years"/>
		<distancefactors selected="false" units="Miles"/>
		<massfactors selected="true" units="Grams" energyunits="KiloJoules"/>
	</outputfactors>
	<savedata>

	</savedata>

	<donotexecute>

		<class name="gov.epa.otaq.moves.master.framework.EmissionCalculator"/>
		<class name="gov.epa.otaq.moves.master.implementation.general.MeteorologyGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.AverageSpeedOperatingModeDistributionGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.EvaporativeEmissionsOperatingModeDistributionGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.FuelEffectsGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.internalcontrolstrategies.onroadretrofit.OnRoadRetrofitStrategy"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.internalcontrolstrategies.rateofprogress.RateOfProgressStrategy"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.LinkOperatingModeDistributionGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.MesoscaleLookupOperatingModeDistributionGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.OperatingModeDistributionGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.ProjectTAG"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.SourceBinDistributionGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.StartOperatingModeDistributionGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.TankFuelGenerator"/>
		<class name="gov.epa.otaq.moves.master.implementation.ghg.TankTemperatureGenerator"/>
	</donotexecute>

	<generatordatabase shouldsave="false" servername="" databasename="" description=""/>
		<donotperformfinalaggregation selected="false"/>
	<lookuptableflags scenarioid="" truncateoutput="false" truncateactivity="false"/>
</runspec>


"""


