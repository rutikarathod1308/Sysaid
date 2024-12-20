import frappe

def custom_before_naming(doc, method):
    # Initialize an empty list to hold the parts of the name
    name_parts = []

    # Add "CM" as the first part of the naming series
    cm_name = "CM"
    name_parts.append(cm_name)

    # Add the state code and category code without separators
    if doc.custom_state_code:
        name_parts.append(doc.custom_state_code)
    if doc.custom_category_code:
        name_parts.append(doc.custom_category_code)

    # Generate the vendor code based on customer_name
    if doc.customer_name:
        first_letter = doc.customer_name[0].upper()  # Use uppercase for consistency
        alphabet_code = frappe.db.get_value("Vendor Code", first_letter, "alphabet_code")

        if alphabet_code is not None:
            # Increment the alphabet_code
            new_vendor_code = int(alphabet_code) + 1
            name_parts.append(f"{first_letter}{new_vendor_code:02}")  # Ensure two digits with leading zeros

            # Update the Vendor Code record with the new alphabet_code
            frappe.db.set_value("Vendor Code", {"name": first_letter}, "alphabet_code", new_vendor_code)
        else:
            # Handle case where alphabet_code is not found
            frappe.throw(f"No alphabet code found for the letter '{first_letter}' in 'Vendor Code'.")

    # Add segment code and additional code without separators
    if doc.custom_segment_code:
        name_parts.append(doc.custom_segment_code)
    if doc.custom_additional_code:
        name_parts.append(doc.custom_additional_code)

    # Concatenate all parts without separators
    doc.custom_customer_code = "".join(name_parts)
