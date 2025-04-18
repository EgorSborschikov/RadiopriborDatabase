from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class OrderStatus(Base):
    __tablename__ = 'order_status'
    status_id = Column(Integer, primary_key=True)
    status_name = Column(String, unique=True, nullable=False)
    orders = relationship("Order", back_populates="status")

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    order_date = Column(Date)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    status_id = Column(Integer, ForeignKey('order_status.status_id'))
    parts = relationship("OrderPart", back_populates="order")
    employees = relationship("EmployeeOrder", back_populates="order")
    quality_controls = relationship("QualityControl", back_populates="order")
    status = relationship("OrderStatus", back_populates="orders")

class Part(Base):
    __tablename__ = 'parts'
    part_id = Column(Integer, primary_key=True)
    part_name = Column(String)
    part_description = Column(String)
    tech_cards = relationship("TechCard", back_populates="part")
    order_parts = relationship("OrderPart", back_populates="part")

class TechCard(Base):
    __tablename__ = 'tech_cards'
    tech_card_id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('parts.part_id'))
    operations = Column(String)
    part = relationship("Part", back_populates="tech_cards")
    machine_programs = relationship("MachineProgram", back_populates="tech_card")

class MachineProgram(Base):
    __tablename__ = 'machine_programs'
    program_id = Column(Integer, primary_key=True)
    tech_card_id = Column(Integer, ForeignKey('tech_cards.tech_card_id'))
    program_code = Column(String)
    tech_card = relationship("TechCard", back_populates="machine_programs")
    equipment_programs = relationship("EquipmentProgram", back_populates="machine_program")

class Employee(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    orders = relationship("EmployeeOrder", back_populates="employee")

class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True)
    department_name = Column(String)
    employees = relationship("Employee", back_populates="department")

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    contact_info = Column(String)
    orders = relationship("Order", back_populates="customer")

class QualityControl(Base):
    __tablename__ = 'quality_control'
    qc_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    qc_status = Column(String)
    qc_date = Column(Date)
    order = relationship("Order", back_populates="quality_controls")

class OrderPart(Base):
    __tablename__ = 'order_parts'
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    part_id = Column(Integer, ForeignKey('parts.part_id'), primary_key=True)
    quantity = Column(Integer)
    order = relationship("Order", back_populates="parts")
    part = relationship("Part", back_populates="order_parts")

class EmployeeOrder(Base):
    __tablename__ = 'employee_orders'
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    role = Column(String)
    employee = relationship("Employee", back_populates="orders")
    order = relationship("Order", back_populates="employees")

class Equipment(Base):
    __tablename__ = 'equipment'
    equipment_id = Column(Integer, primary_key=True)
    equipment_name = Column(String)
    equipment_type = Column(String)
    equipment_programs = relationship("EquipmentProgram", back_populates="equipment")

class EquipmentProgram(Base):
    __tablename__ = 'equipment_programs'
    equipment_id = Column(Integer, ForeignKey('equipment.equipment_id'), primary_key=True)
    program_id = Column(Integer, ForeignKey('machine_programs.program_id'), primary_key=True)
    assignment_date = Column(Date)
    equipment = relationship("Equipment", back_populates="equipment_programs")
    machine_program = relationship("MachineProgram", back_populates="equipment_programs")

class Supplier(Base):
    __tablename__ = 'suppliers'
    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String)
    contact_info = Column(String)
    supplies = relationship("Supply", back_populates="supplier")

class Supply(Base):
    __tablename__ = 'supplies'
    supply_id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    part_id = Column(Integer, ForeignKey('parts.part_id'))
    supply_date = Column(Date)
    quantity = Column(Integer)
    supplier = relationship("Supplier", back_populates="supplies")
    part = relationship("Part", back_populates="supplies")