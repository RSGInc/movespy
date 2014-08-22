<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html"/>    

<xsl:key name="gid_key" match="*" use="generate-id()"/>

<xsl:template match="/">
    <xsl:call-template name="index"/>
    <xsl:call-template name="content"/>
</xsl:template>

<xsl:template name="index">
    <xsl:variable name="all-r" select="//line[contains(@string,'Simulation started')]"/>

    <xsl:if test="count($all-r) &gt; 1">
        <table>
            <tr><td align="center" bgcolor="#aaaaff"><b>INDEX</b></td></tr>
            <tr><td>
            <a name="TOC"> </a>
            <table border="1" cellspacing="0">
            <xsl:for-each select="$all-r"> 
                <xsl:sort select="position()" order="descending" data-type="number"/>  
                <tr><td class="direction"><a href="#{generate-id()}"><xsl:value-of select="@string"/></a></td></tr>
            </xsl:for-each>
            </table></td></tr>
        </table>
        <p></p>
    </xsl:if>
</xsl:template>


<xsl:template name="content">
    <xsl:variable name="all-r" select="//line[contains(@string,'Simulation started') or position()=1]"/>

    <xsl:for-each select="$all-r"> 
        <xsl:variable name="header_id" select="generate-id()"/>
        <xsl:variable name="next_header_id" select="generate-id(following::*[contains(@string,'Simulation started')])"/>
        <xsl:variable name="next_header_pos">
            <xsl:for-each select="following::*">
                <xsl:if test="generate-id() = $next_header_id">
                    <xsl:value-of select="position()"/>
                </xsl:if>
            </xsl:for-each>
            <xsl:if test="$next_header_id=''">
                <xsl:value-of select="count(following::*) + 1"/>
            </xsl:if>
        </xsl:variable>
        <table><tr><td bgcolor="#dddddd"><a name="#{$header_id}">
            <xsl:if test="contains(@string,'Simulation started')">  
                <xsl:value-of select="@string"/>
            </xsl:if>
        </a></td></tr></table>
        <xsl:call-template name="run">
            <xsl:with-param name="lines" select="following::*[position() &lt; $next_header_pos]"/>
        </xsl:call-template>
    </xsl:for-each>
</xsl:template>

<xsl:key name="tsm_group_key" match="//line[starts-with(normalize-space(@string), '[')]" 
    use="substring-after(substring-before(normalize-space(@string),']'),'[')"/>
<xsl:key name="tsm_no_group_key" match="//line[not(starts-with(normalize-space(@string), '['))]" 
    use="."/>

<xsl:template name="run">
    <xsl:param name="lines"/>

    <xsl:variable name="group-names" select="//line[generate-id(.)=generate-id(key('tsm_group_key',
            substring-after(substring-before(normalize-space(@string),']'),'[')))]"/> 

    <xsl:if test="count($lines)=0">
        No messages<br/>
    </xsl:if>

    <xsl:for-each select="$group-names"> 
        <xsl:variable name="curr-group" select="substring-after(substring-before(normalize-space(@string),']'),'[')"/>

        <xsl:variable name="group-lines" select="$lines[
            substring-after(substring-before(normalize-space(@string),']'),'[')=$curr-group]"/> 
        
        <xsl:if test="count($group-lines) &gt; 0">
            <h4><xsl:value-of select="$curr-group"/></h4>
            <xsl:for-each select="$group-lines"> 
                <xsl:value-of select="concat(translate(substring-after(@string,']'),' ','&#x20;'), '&#x0A;')"/>
                <br/>
            </xsl:for-each>
        </xsl:if>
    </xsl:for-each>

    <xsl:variable name="misc-lines" select="$lines[not(starts-with(normalize-space(@string), '['))]"/> 

    <xsl:if test="count($misc-lines) &gt; 0">
        <h4><xsl:value-of select="'Misc'"/></h4>

        <xsl:for-each select="$misc-lines"> 
            <xsl:value-of select="concat(translate(@string,' ','&#x20;'), '&#x0A;')"/>
            <br/>
        </xsl:for-each>
    </xsl:if>
    <br/>
</xsl:template>

</xsl:stylesheet>

