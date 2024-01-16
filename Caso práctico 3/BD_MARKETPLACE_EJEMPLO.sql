CREATE DATABASE MARKETPLACE;
CREATE TABLE Users (
  UserID INT PRIMARY KEY,
  Username VARCHAR(50),
  Email VARCHAR(50),
  Password VARCHAR(50)
);

CREATE TABLE Products (
  ProductID INT PRIMARY KEY,
  SellerID INT,
  Name VARCHAR(50),
  Description TEXT,
  Price DECIMAL(10,2),
  FOREIGN KEY (SellerID) REFERENCES Users(UserID)
);

CREATE TABLE Orders (
  OrderID INT PRIMARY KEY,
  BuyerID INT,
  ProductID INT,
  Quantity INT,
  OrderDate DATE,
  FOREIGN KEY (BuyerID) REFERENCES Users(UserID),
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);