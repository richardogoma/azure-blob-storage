# ------------------------

az account list 

az group list 

az resource list 

wget https://github.com/MicrosoftDocs/mslearn-connect-app-to-azure-storage/blob/main/images/docs-and-friends-selfie-stick.png?raw=true -O docs-and-friends-selfie-stick.png

# -----------------------------------
az storage account create \
  --name richarddemoaccount01 \
  --resource-group learn-6c8009b4-5066-440c-ad4a-26dcc13d5b8b \
  --location westeurope \
  --sku Standard_LRS \
  --kind StorageV2 \
  --allow-blob-public-access true \
  --public-network-access Enabled

az storage account show-connection-string \
  --resource-group learn-0671187d-0571-41b8-a829-91a0f9f49e02 \
  --query connectionString \
  --name richarddemoaccount01


az storage account show-connection-string --name "richarddemoaccount01"

az storage container list \
  --account-name richarddemoaccount01


