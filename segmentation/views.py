from django.shortcuts import render
import os
import pickle
import pandas as pd
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage

# Load the ML model
MODEL_PATH = os.path.join(settings.BASE_DIR, 'segmentation/kmeans_model.pkl')
with open(MODEL_PATH, 'rb') as file:
    kmeans_model = pickle.load(file)

# Directory to save processed CSV files
OUTPUT_DIR = os.path.join(settings.BASE_DIR, 'segmentation/output_csvs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# View for the main dashboard
def main(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file:
            return JsonResponse({'error': 'No file uploaded.'}, status=400)

        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'Invalid file type. Please upload a CSV file.'}, status=400)

        try:
            # Read the uploaded CSV file
            data = pd.read_csv(csv_file)

            # Check for the required column
            if 'Total_Selling' not in data.columns:
                return JsonResponse({'error': "'Total_Selling' column is missing in the uploaded file."}, status=400)

            # Define thresholds for segmentation
            low_threshold = data['Total_Selling'].quantile(1 / 3)
            high_threshold = data['Total_Selling'].quantile(2 / 3)

            # Segment the data
            low_sales = data[data['Total_Selling'] <= low_threshold]
            mid_sales = data[(data['Total_Selling'] > low_threshold) & (data['Total_Selling'] <= high_threshold)]
            high_sales = data[data['Total_Selling'] > high_threshold]

            # Save segmented data to CSV files
            high_sales_file = os.path.join(settings.MEDIA_ROOT, 'High_Selling_Products.csv')
            mid_sales_file = os.path.join(settings.MEDIA_ROOT, 'Mid_Selling_Products.csv')
            low_sales_file = os.path.join(settings.MEDIA_ROOT, 'Low_Selling_Products.csv')

            #Index not including 
            high_sales.to_csv(high_sales_file, index=False)
            mid_sales.to_csv(mid_sales_file, index=False)
            low_sales.to_csv(low_sales_file, index=False)
            
            #Showing Top 5 Rows
            high_top = high_sales.head(5).to_dict(orient='records')
            mid_top = mid_sales.head(5).to_dict(orient='records')
            low_top = low_sales.head(5).to_dict(orient='records')

            # Redirect user to a page showing download links and top rows
            return render(request, 'segmentation/result.html', {
                'high_sales_csv': "High_Selling_Products.csv",
                'mid_sales_csv': "Mid_Selling_Products.csv",
                'low_sales_csv': "Low_Selling_Products.csv",
                'high_top': high_top,
                'mid_top': mid_top,
                'low_top': low_top,
            })

        except Exception as e:
            return JsonResponse({'error': f"Error processing file: {e}"}, status=500)

    return render(request, 'segmentation/main.html')


# Download processed CSV
def download_csv(request, filename):
    file_path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as csv_file:
            response = HttpResponse(csv_file.read(), content_type='text/csv')
            response['Content-Disposition'] = f'inline; filename="{filename}"'
            return response
    else:
        return JsonResponse({'error': 'File not found.'}, status=404)


# Basic views for login, signup, and index
def landing(request):
    return render(request, 'segmentation/landing.html')

def login(request):
    return render(request, 'segmentation/login.html')

def signup(request):
    return render(request, 'segmentation/signup.html')

def StockInfo(request):
    return render(request, 'segmentation/StockInfo.html')

def navbar(request):
    return render(request, 'segmentation/navbar.html')

def help(request):
    return render(request, 'segmentation/help.html')

def contactus(request):
    return render(request, 'segmentation/contactus.html')

def PrivacyPolicy(request):
    return render(request, 'segmentation/PrivacyPolicy.html')

def TermsOfService(request):
    return render(request, 'segmentation/TermsOfService.html')