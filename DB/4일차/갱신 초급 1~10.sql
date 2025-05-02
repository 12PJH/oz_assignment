-- customers 테이블에서 특정 고객의 주소를 갱신하세요.
update customers set addressLine1 = '054 pohang st';

-- products 테이블에서 특정 제품의 가격을 갱신하세요.
update products set buyprice = 100 where productCode = 'S12_1099';

-- employees 테이블에서 특정 직원의 직급를 갱신하세요.
update employees set jobTitle = 'CEO' where officecode = '2';

-- offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
update offices set phone = '010-1234-5678' where officeCode = '1';

-- orders 테이블에서 특정 주문 상태를 갱신하세요.
update orders set status = 'on hold' where orderNumber = 10040;

-- orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
update orderdetails set quantityordered = 15 where orderNumber = 10040;

-- payments 테이블에서 특정 지불의 금액을 갱신하세요.
update payments set amount = 1004.0000 where customerNumber = 103;

-- productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
update productlines set textDescription = 'Very delicious and spicy' where productline = 'Korean Food';

-- customers 테이블에서 특정 고객의 이메일을 갱신하세요.
update customers set customers_email = 'oz@gmail.com' where customerNumber = 100;

-- products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
update products set buyprice = 9999.99;