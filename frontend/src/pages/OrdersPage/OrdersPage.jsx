import { MainNav } from "@/components/MainNav";

import { Input } from "../../components/ui/Input"
import { Form } from "../../components/ui/Form"
import { Button } from "../../components/ui/Button"
import { DataTable } from "./components/DataTable";
import { Columns } from "./components/Columns";
import { UserNav } from "./components/UserNav";
import { navigationLinks } from "../../config/navigationLinks";
import { useEffect, useState } from "react";

export const OrdersPage = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/orders")
      .then((response) => response.json())
      .then((data) => {
        setData(data)
        console.log(data)
      });
  }, []);

  const [customer_id, setCustomerId] = useState("");
  const [products_id, setProductsId] = useState("");
  const [quantity, setQuantity] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(customer_id, products_id, quantity)

    fetch("http://127.0.0.1:8000/orders/", {
      method:"POST",
      headers:{
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"customer_id": customer_id, "products_id": products_id, "quantity": quantity})
    }).then((response) => response.json())
      .then((data) => console.log(data));

    setCustomerId("");
    setProductsId("");
    setQuantity("");
  }

  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <MainNav className="mx-6" links={navigationLinks} />
          <div className="ml-auto flex items-center space-x-4">
            <UserNav />
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Orders</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex">
          <DataTable
            data={data}
            columns={Columns}
          />
        </div>
      </div>
    </div>
  );
};
