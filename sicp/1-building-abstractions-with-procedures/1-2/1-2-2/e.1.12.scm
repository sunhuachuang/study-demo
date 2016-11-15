;; pascal
;; f(x, y) = f(x-1, y-1) + f(x, y-1)  x=col y=row

;; recursive
(define (pascal-recu x y)
  (if (or (= x 1) (= y 1) (= x y))
      1
      (+ (pascal-recu (- x 1) (- y 1))
         (pascal-recu x (- y 1)))))

(pascal-recu 3 5) ;;6

;; iteration
;; f(x, y) = x!(y-x)!/y!
