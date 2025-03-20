import frappe

def item_before_naming(doc, method):
    if doc.custom_is_item_specification == 1 :
    # Initialize an empty list to hold the parts of the name
        name_parts = []

        # Add "CM" as the first part of the naming series
        

        # Add the state code and category code without separators
        if doc.custom_product_short_name:
            name_parts.append(doc.custom_product_short_name)
        if doc.custom_pruduct_information:
            name_parts.append(doc.custom_pruduct_information)
        if doc.custom_revision_no:
            name_parts.append(doc.custom_revision_no)
        if doc.custom_customer_code_name:
            name_parts.append(doc.custom_customer_code_name)
        if doc.custom_variation__model_code:
            name_parts.append(doc.custom_variation__model_code)
        if doc.custom_additional_inform_code:
            name_parts.append(doc.custom_additional_inform_code)
        # Generate the vendor code based on customer_name
        
        # Concatenate all parts without separators
        doc.item_code = "".join(name_parts)
