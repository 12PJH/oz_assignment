-- customers 테이블에 새 고객을 추가하세요.
insert into customers (customerNumber, customerName, contactLastName) VALUES (123,'Jun Hyuk', 'park');

-- products 테이블에 새 제품을 추가하세요.
insert into products (productCode, productName, productLine) Values (123, 'santafe','Classic Cars');

-- employees 테이블에 새 직원을 추가하세요.
insert into employees (employeeNumber, lastName, firstName) Values (1004, 'Jun hyuk','Park');

-- offices 테이블에 새 사무실을 추가하세요.
insert into offices (officeCode, city, phone, country) Values (8, 'seoul', '82+ 010 1234 5678', 'korea');

-- orders 테이블에 새 주문을 추가하세요.
insert into orders (orderNumber, orderDate) values (10040, '2025-05-02');

-- orderdetails 테이블에 주문 상세 정보를 추가하세요.
insert into orderdetails (orderNumber, productCode) values (10040, 'S18_1984');

-- payments 테이블에 지불 정보를 추가하세요.
insert into payments (customerNumber,checkNumber, amount, paymentdate) values (123,200.00,100, '2025-05-25');

-- productlines 테이블에 제품 라인을 추가하세요.
insert into products (productLine) values ('Korean Food');

-- customers 테이블에 다른 지역의 고객을 추가하세요.
insert into customers (customerNumber, customerName, contactLastName, country) values (100, 'gildong', 'Hong', 'Joseon');

-- products 테이블에 다른 카테고리의 제품을 추가하세요.
insert into products (productCode, productName, productLine) values ('1004','Pork belly','Korean Food');




