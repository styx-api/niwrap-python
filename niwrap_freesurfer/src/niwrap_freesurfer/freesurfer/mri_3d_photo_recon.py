# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_3D_PHOTO_RECON_METADATA = Metadata(
    id="1da2f095a43ac3c7dfc286883ae9220b1018660e.boutiques",
    name="mri_3d_photo_recon",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Mri3dPhotoReconParameters = typing.TypedDict('Mri3dPhotoReconParameters', {
    "__STYX_TYPE__": typing.Literal["mri_3d_photo_recon"],
    "input_photo_dir": list[InputPathType],
    "input_segmentation_dir": list[InputPathType],
    "slice_thickness": float,
    "photo_resolution": float,
    "output_directory": str,
    "ref_mask": typing.NotRequired[InputPathType | None],
    "ref_surface": typing.NotRequired[InputPathType | None],
    "ref_soft_mask": typing.NotRequired[InputPathType | None],
    "mesh_reorient_with_indices": typing.NotRequired[str | None],
    "photos_posterior_side": bool,
    "order_posterior_to_anterior": bool,
    "allow_z_stretch": bool,
    "rigid_only_for_photos": bool,
    "gpu_index": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_3d_photo_recon": mri_3d_photo_recon_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_3d_photo_recon": mri_3d_photo_recon_outputs,
    }.get(t)


class Mri3dPhotoReconOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_3d_photo_recon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reconstructed_volume: OutputPathType
    """Reconstructed photo volume output file"""
    reference_data: OutputPathType
    """Output reference data"""


def mri_3d_photo_recon_params(
    input_photo_dir: list[InputPathType],
    input_segmentation_dir: list[InputPathType],
    slice_thickness: float,
    photo_resolution: float,
    output_directory: str,
    ref_mask: InputPathType | None = None,
    ref_surface: InputPathType | None = None,
    ref_soft_mask: InputPathType | None = None,
    mesh_reorient_with_indices: str | None = None,
    photos_posterior_side: bool = False,
    order_posterior_to_anterior: bool = False,
    allow_z_stretch: bool = False,
    rigid_only_for_photos: bool = False,
    gpu_index: float | None = None,
) -> Mri3dPhotoReconParameters:
    """
    Build parameters.
    
    Args:
        input_photo_dir: Directory with input photos (required).
        input_segmentation_dir: Directory with input slab masks / segmentations\
            (required).
        slice_thickness: Slice thickness in mm.
        photo_resolution: Resolution of the photos in mm.
        output_directory: Output directory with reconstructed photo volume and\
            reference.
        ref_mask: Reference binary mask.
        ref_surface: Reference surface file.
        ref_soft_mask: Reference soft mask.
        mesh_reorient_with_indices: Vertex indices of frontal pole, occipital\
            pole, and top of central sulcus, separated with commas, for mesh\
            alignment.
        photos_posterior_side: Use when photos are taken of posterior side of\
            slabs (default is anterior side).
        order_posterior_to_anterior: Use when photos are ordered from posterior\
            to anterior (default is anterior to posterior).
        allow_z_stretch: Use to adjust the slice thickness to best match the\
            reference. You should probably *never* use this with soft references\
            (ref_soft_mask).
        rigid_only_for_photos: Switch on if you want photos to deform only\
            rigidly (not affine).
        gpu_index: Index of GPU to use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_3d_photo_recon",
        "input_photo_dir": input_photo_dir,
        "input_segmentation_dir": input_segmentation_dir,
        "slice_thickness": slice_thickness,
        "photo_resolution": photo_resolution,
        "output_directory": output_directory,
        "photos_posterior_side": photos_posterior_side,
        "order_posterior_to_anterior": order_posterior_to_anterior,
        "allow_z_stretch": allow_z_stretch,
        "rigid_only_for_photos": rigid_only_for_photos,
    }
    if ref_mask is not None:
        params["ref_mask"] = ref_mask
    if ref_surface is not None:
        params["ref_surface"] = ref_surface
    if ref_soft_mask is not None:
        params["ref_soft_mask"] = ref_soft_mask
    if mesh_reorient_with_indices is not None:
        params["mesh_reorient_with_indices"] = mesh_reorient_with_indices
    if gpu_index is not None:
        params["gpu_index"] = gpu_index
    return params


def mri_3d_photo_recon_cargs(
    params: Mri3dPhotoReconParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mri_3d_photo_recon")
    cargs.extend([
        "--input_photo_dir",
        *[execution.input_file(f) for f in params.get("input_photo_dir")]
    ])
    cargs.extend([
        "--input_segmentation_dir",
        *[execution.input_file(f) for f in params.get("input_segmentation_dir")]
    ])
    cargs.extend([
        "--slice_thickness",
        str(params.get("slice_thickness"))
    ])
    cargs.extend([
        "--photo_resolution",
        str(params.get("photo_resolution"))
    ])
    cargs.extend([
        "--output_directory",
        params.get("output_directory")
    ])
    if params.get("ref_mask") is not None:
        cargs.extend([
            "--ref_mask",
            execution.input_file(params.get("ref_mask"))
        ])
    if params.get("ref_surface") is not None:
        cargs.extend([
            "--ref_surface",
            execution.input_file(params.get("ref_surface"))
        ])
    if params.get("ref_soft_mask") is not None:
        cargs.extend([
            "--ref_soft_mask",
            execution.input_file(params.get("ref_soft_mask"))
        ])
    if params.get("mesh_reorient_with_indices") is not None:
        cargs.extend([
            "--mesh_reorient_with_indices",
            params.get("mesh_reorient_with_indices")
        ])
    if params.get("photos_posterior_side"):
        cargs.append("--photos_of_posterior_side")
    if params.get("order_posterior_to_anterior"):
        cargs.append("--order_posterior_to_anterior")
    if params.get("allow_z_stretch"):
        cargs.append("--allow_z_stretch")
    if params.get("rigid_only_for_photos"):
        cargs.append("--rigid_only_for_photos")
    if params.get("gpu_index") is not None:
        cargs.extend([
            "--gpu",
            str(params.get("gpu_index"))
        ])
    return cargs


def mri_3d_photo_recon_outputs(
    params: Mri3dPhotoReconParameters,
    execution: Execution,
) -> Mri3dPhotoReconOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Mri3dPhotoReconOutputs(
        root=execution.output_file("."),
        reconstructed_volume=execution.output_file(params.get("output_directory") + "/reconstructed_volume.nii.gz"),
        reference_data=execution.output_file(params.get("output_directory") + "/reference_data.nii.gz"),
    )
    return ret


def mri_3d_photo_recon_execute(
    params: Mri3dPhotoReconParameters,
    execution: Execution,
) -> Mri3dPhotoReconOutputs:
    """
    Code for 3D photo reconstruction (Tregidgo, et al., MICCAI 2020).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Mri3dPhotoReconOutputs`).
    """
    params = execution.params(params)
    cargs = mri_3d_photo_recon_cargs(params, execution)
    ret = mri_3d_photo_recon_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_3d_photo_recon(
    input_photo_dir: list[InputPathType],
    input_segmentation_dir: list[InputPathType],
    slice_thickness: float,
    photo_resolution: float,
    output_directory: str,
    ref_mask: InputPathType | None = None,
    ref_surface: InputPathType | None = None,
    ref_soft_mask: InputPathType | None = None,
    mesh_reorient_with_indices: str | None = None,
    photos_posterior_side: bool = False,
    order_posterior_to_anterior: bool = False,
    allow_z_stretch: bool = False,
    rigid_only_for_photos: bool = False,
    gpu_index: float | None = None,
    runner: Runner | None = None,
) -> Mri3dPhotoReconOutputs:
    """
    Code for 3D photo reconstruction (Tregidgo, et al., MICCAI 2020).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_photo_dir: Directory with input photos (required).
        input_segmentation_dir: Directory with input slab masks / segmentations\
            (required).
        slice_thickness: Slice thickness in mm.
        photo_resolution: Resolution of the photos in mm.
        output_directory: Output directory with reconstructed photo volume and\
            reference.
        ref_mask: Reference binary mask.
        ref_surface: Reference surface file.
        ref_soft_mask: Reference soft mask.
        mesh_reorient_with_indices: Vertex indices of frontal pole, occipital\
            pole, and top of central sulcus, separated with commas, for mesh\
            alignment.
        photos_posterior_side: Use when photos are taken of posterior side of\
            slabs (default is anterior side).
        order_posterior_to_anterior: Use when photos are ordered from posterior\
            to anterior (default is anterior to posterior).
        allow_z_stretch: Use to adjust the slice thickness to best match the\
            reference. You should probably *never* use this with soft references\
            (ref_soft_mask).
        rigid_only_for_photos: Switch on if you want photos to deform only\
            rigidly (not affine).
        gpu_index: Index of GPU to use.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Mri3dPhotoReconOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_3D_PHOTO_RECON_METADATA)
    params = mri_3d_photo_recon_params(
        input_photo_dir=input_photo_dir,
        input_segmentation_dir=input_segmentation_dir,
        slice_thickness=slice_thickness,
        photo_resolution=photo_resolution,
        output_directory=output_directory,
        ref_mask=ref_mask,
        ref_surface=ref_surface,
        ref_soft_mask=ref_soft_mask,
        mesh_reorient_with_indices=mesh_reorient_with_indices,
        photos_posterior_side=photos_posterior_side,
        order_posterior_to_anterior=order_posterior_to_anterior,
        allow_z_stretch=allow_z_stretch,
        rigid_only_for_photos=rigid_only_for_photos,
        gpu_index=gpu_index,
    )
    return mri_3d_photo_recon_execute(params, execution)


__all__ = [
    "MRI_3D_PHOTO_RECON_METADATA",
    "Mri3dPhotoReconOutputs",
    "Mri3dPhotoReconParameters",
    "mri_3d_photo_recon",
    "mri_3d_photo_recon_params",
]
