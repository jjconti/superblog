<html><body><p>Estoy usando <a href="http://www.gnu.org/software/emacs/">emacs</a> para practicar <a href="http://www.python.org">python</a>. 

En ~/.emacs.d/ guardé <a href="http://sourceforge.net/projects/python-mode/">python-mode.el</a> y en ~/.emacs tengo estas líenas:

</p><pre lang="lisp">

(setq load-path (cons (expand-file-name "~/.emacs.d") load-path ))

(require 'python-mode)

(nconc auto-mode-alist '(("\\.py\\'" . python-mode)))

</pre>

Cuando abro un archivo llamado *.py puedo tipear M-x font-lock-fontify-buffer[enter] y tener la sintaxis coloreada.

</body></html>