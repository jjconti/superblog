<html><body><p>At <a href="https://watuapp.com/" target="_blank">Watu</a>, we have just released a new version of <a href="https://rubygems.org/gems/mail_safe" target="_blank">mail_safe gem</a> (originally developed by <a href="http://myronmars.to/" target="_blank">Myron Marston</a>).

</p><blockquote>Mail safe provides a safety net while you're developing an application that uses ActionMailer. It keeps emails from escaping into the wild. Once you've installed and configured this gem, you can rest assure that your app won"t send emails to external email addresses. Instead, emails that would normally be delivered to external addresses will be sent to an address of your choosing, and the body of the email will be appended with a note stating where the email was originally intended to go.</blockquote>

<h2>Changelog for 0.3.2 version</h2>

<ul>

	<li>Updated to manage the gem using bundler.</li>

	<li>Updated to run tests with RSpec 3.</li>

	<li>Updated to support actionmailer &gt;= 3.2 (support for older versions was removed to simplify code).</li>

	<li>Changed ginger in favor of <a href="https://github.com/thoughtbot/appraisal" target="_blank">appraisal</a> to test the gem against different versions of actionmailer.</li>

	<li>Added support for continuous integrations with <a href="https://travis-ci.org/watu/mail_safe" target="_blank">Travis</a> (can be locally emulated with <a href="https://github.com/grosser/wwtd" target="_blank">wwtd</a>).</li>

	<li>Fixed <a href="https://github.com/myronmarston/mail_safe/issues/7" target="_blank">https://github.com/myronmarston/mail_safe/issues/7</a></li>

	<li>Fixed <a href="https://github.com/myronmarston/mail_safe/issues/3" target="_blank">https://github.com/myronmarston/mail_safe/issues/3</a></li>

	<li>Updated <a href="https://github.com/myronmarston/mail_safe" target="_blank">source code page</a> with some fancy badges.</li>

</ul>

<h2>Thanks</h2>

Thanks <a href="https://watuapp.com/" target="_blank">Watu</a> for funding this release and <a href="http://myronmars.to/" target="_blank">Myron</a> for the support!

<h2>Update</h2>

0.3.3 has just been released (17th of september) to make coveralls a development dependency instead of a deployment one.</body></html>