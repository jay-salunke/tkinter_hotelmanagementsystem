def add_data(self):
        if(self.form_validation()):
            try:
                db_cursor = self.db_con.db.cursor()
                db_cursor.execute("insert into customers_details(ref_id,customer_name,customer_email_id,customer_mobile_no,customer_nationality,customer_state,customer_gender,customer_proof_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.id.get(),
                    self.name.get(),
                    self.email_id.get(),
                    self.mobile_no.get(),
                    self.nationality.get(),
                    self.state.get(),
                    self.gender.get(),
                    self.proof_type.get()
                ))
                self.db_con.db.commit()
                self.engine.say("Data inserted successfully")
                self.engine.runAndWait()
                self.fetch_data()
                messagebox.showinfo(
                    "Success", "Data inserted successfully", parent=self.root)

            except Exception as e:
                self.db_con.db.rollback()
                messagebox.showwarning(
                    "Warning", f"{str(e)}", parent=self.root)
        return

    def fetch_data(self):
        try:
            db_cursor = self.db_con.db.cursor()
            db_cursor.execute("select * from customers_details")
            rows = db_cursor.fetchall()
            if len(rows) != 0:
                self.customer_details_table.delete(
                    *self.customer_details_table.get_children())
                for i in rows:
                    self.customer_details_table.insert("", END, values=i)
                self.db_con.db.commit()
            db_cursor.close()
            self.db_con.db.close()
        except Exception as e:
            messagebox.showerror("Error", f"{self.db_con.db.rollback()}")
            print(e)
        return