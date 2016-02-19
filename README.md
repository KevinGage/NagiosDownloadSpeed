# NagiosDownloadSpeed

<h1>Install</h1>
<ol>
<li>sudo apt-get install python-pip</li>
<li>sudo pip install speedtest-cli</li>
<li>Copy check_dowloadspeed.py to /usr/local/nagios/libexec/</li>
<li>chmod +x /usr/local/nagios/libexec/check_downloadspeed.py</li>
<li>Copy check_downloadspeed.cfg to /usr/local/nagios/etc/commands/</li>
<li>Copy downloadspeed.cfg to /usr/local/nagios/etc/services/</li>
<li>Edit /usr/local/nagios/etc/services/downloadspeed.cfg</li>
  <ul>
  <li>Remove "srv-pnp" if pnp4nagios is not installed</li>
  <li>edit check command.  First number should be download speed for a warning, second should be cricitical download speed</li>
  <li>Remove noticications enabled if this is a remote node</li>
  <li>set appropriate check interval in minutes</li>
  </ul>
</ol>
