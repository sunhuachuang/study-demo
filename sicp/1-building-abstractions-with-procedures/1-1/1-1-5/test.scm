(define (p) (p))

(define (test x y)
  (if (= x 0)
      0
      y))
(test 0 (p))
;;正则序　0
;;应用序　循环调用ｐ
