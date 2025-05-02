-- customers 테이블에서 특정 고객을 삭제하세요.
delete from customers where customernumber = 100;

-- products 테이블에서 특정 제품을 삭제하세요.
delete from products where productcode = '123';

-- employees 테이블에서 특정 직원을 삭제하세요.
delete from employees where employeeNumber = 1004;

-- offices 테이블에서 특정 사무실을 삭제하세요.
delete from offices where officeCode = '8';

-- orders 테이블에서 특정 주문을 삭제하세요.
delete from orders where orderNumber = 10100;

-- orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
delete from orderdetails where ordernumber = 10040;

-- payments 테이블에서 특정 지불 내역을 삭제하세요.
delete from payments where customerNumber = 103;

-- productlines 테이블에서 특정 제품 라인을 삭제하세요.
delete from productlines where productline = 'Korean Food';

-- customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
delete from customers where country = 'Korea';

-- products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
delete from products where productline = 'Classic Car';