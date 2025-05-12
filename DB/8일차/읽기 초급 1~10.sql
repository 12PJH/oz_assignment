-- customers 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;

-- products 테이블에서 모든 제품 목록을 조회하세요.
select * from products;

-- employees 테이블에서 모든 제품 목록을 조회하세요.
select * from employees;

-- offices 테이블에서 모든 사무실 위치를 조회하세요.
select addressLine1, addressLine2 from offices;

-- orders 테이블에서 최근 10개의 주문을 조회하세요.
select * from orders order by orderdate desc limit 10;

-- orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from orderdetails where 조건 = 값;

-- payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments where customerNumber = '고객의 번호';

-- customers 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where country = '나라이름';

-- products 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where buyPrice between x and y; -- price > , = , < x