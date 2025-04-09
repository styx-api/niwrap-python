# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

OXFORD_ASL_METADATA = Metadata(
    id="bdbf1ed97eaa86bb7fae170ece4a5bc7b7b7a7f8.boutiques",
    name="oxford_asl",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


OxfordAslParameters = typing.TypedDict('OxfordAslParameters', {
    "__STYX_TYPE__": typing.Literal["oxford_asl"],
    "asl_data": InputPathType,
    "output_dir_name": str,
    "mask": typing.NotRequired[InputPathType | None],
    "spatial_smoothing": bool,
    "white_paper_analysis": bool,
    "motion_correction": bool,
    "input_asl_format": typing.NotRequired[str | None],
    "input_block_format": typing.NotRequired[str | None],
    "inversion_times": typing.NotRequired[str | None],
    "ti_image": typing.NotRequired[InputPathType | None],
    "casl": bool,
    "arterial_suppression": bool,
    "bolus_duration": typing.NotRequired[float | None],
    "bat": typing.NotRequired[float | None],
    "tissue_t1": typing.NotRequired[float | None],
    "blood_t1": typing.NotRequired[float | None],
    "slice_timing_difference": typing.NotRequired[float | None],
    "slice_band": typing.NotRequired[float | None],
    "flip_angle": typing.NotRequired[float | None],
    "fsl_anat_dir": typing.NotRequired[str | None],
    "structural_image": typing.NotRequired[InputPathType | None],
    "bet_structural_image": typing.NotRequired[InputPathType | None],
    "fast_segmentation_images": typing.NotRequired[str | None],
    "sensitivity_correction": bool,
    "precomputed_m0_value": typing.NotRequired[float | None],
    "inversion_efficiency": typing.NotRequired[float | None],
    "tr_calibration_data": typing.NotRequired[float | None],
    "calibration_image": typing.NotRequired[InputPathType | None],
    "calibration_method": typing.NotRequired[str | None],
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
        "oxford_asl": oxford_asl_cargs,
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
        "oxford_asl": oxford_asl_outputs,
    }.get(t)


class OxfordAslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `oxford_asl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dir: OutputPathType
    """Directory containing the output files"""


def oxford_asl_params(
    asl_data: InputPathType,
    output_dir_name: str,
    mask: InputPathType | None = None,
    spatial_smoothing: bool = False,
    white_paper_analysis: bool = False,
    motion_correction: bool = False,
    input_asl_format: str | None = None,
    input_block_format: str | None = None,
    inversion_times: str | None = None,
    ti_image: InputPathType | None = None,
    casl: bool = False,
    arterial_suppression: bool = False,
    bolus_duration: float | None = None,
    bat: float | None = None,
    tissue_t1: float | None = None,
    blood_t1: float | None = None,
    slice_timing_difference: float | None = None,
    slice_band: float | None = None,
    flip_angle: float | None = None,
    fsl_anat_dir: str | None = None,
    structural_image: InputPathType | None = None,
    bet_structural_image: InputPathType | None = None,
    fast_segmentation_images: str | None = None,
    sensitivity_correction: bool = False,
    precomputed_m0_value: float | None = None,
    inversion_efficiency: float | None = None,
    tr_calibration_data: float | None = None,
    calibration_image: InputPathType | None = None,
    calibration_method: str | None = None,
) -> OxfordAslParameters:
    """
    Build parameters.
    
    Args:
        asl_data: Input ASL data.
        output_dir_name: Output directory name.
        mask: Mask in native space of ASL data.
        spatial_smoothing: Use adaptive spatial smoothing on perfusion.
        white_paper_analysis: Analysis that conforms to the 'white paper'\
            (Alsop et al. 2014).
        motion_correction: Apply motion correction using mcflirt.
        input_asl_format: Input ASL format: diff, tc, ct.
        input_block_format: Input block format (for multi-TI): rpt, tis.
        inversion_times: Comma separated list of inversion times.
        ti_image: 4D image containing voxelwise TI values.
        casl: ASL acquisition is pseudo cASL (pcASL) rather than pASL.
        arterial_suppression: Arterial suppression (vascular crushing) was used.
        bolus_duration: Bolus duration.
        bat: Bolus arrival time.
        tissue_t1: Tissue T1 value.
        blood_t1: Blood T1 value.
        slice_timing_difference: Timing difference between slices.
        slice_band: Number of slices per band in a multi-band setup.
        flip_angle: Flip angle for Look-Locker readout correction.
        fsl_anat_dir: An fsl_anat directory from structural image.
        structural_image: Structural image (whole head).
        bet_structural_image: Structural image (already BETed).
        fast_segmentation_images: Images from a FAST segmentation.
        sensitivity_correction: Use bias field (from segmentation) for\
            sensitivity correction.
        precomputed_m0_value: Single precomputed M0 value.
        inversion_efficiency: Inversion efficiency.
        tr_calibration_data: TR of calibration data.
        calibration_image: M0 calibration image (proton density or mean control\
            image).
        calibration_method: Calibration method: single or voxel.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "oxford_asl",
        "asl_data": asl_data,
        "output_dir_name": output_dir_name,
        "spatial_smoothing": spatial_smoothing,
        "white_paper_analysis": white_paper_analysis,
        "motion_correction": motion_correction,
        "casl": casl,
        "arterial_suppression": arterial_suppression,
        "sensitivity_correction": sensitivity_correction,
    }
    if mask is not None:
        params["mask"] = mask
    if input_asl_format is not None:
        params["input_asl_format"] = input_asl_format
    if input_block_format is not None:
        params["input_block_format"] = input_block_format
    if inversion_times is not None:
        params["inversion_times"] = inversion_times
    if ti_image is not None:
        params["ti_image"] = ti_image
    if bolus_duration is not None:
        params["bolus_duration"] = bolus_duration
    if bat is not None:
        params["bat"] = bat
    if tissue_t1 is not None:
        params["tissue_t1"] = tissue_t1
    if blood_t1 is not None:
        params["blood_t1"] = blood_t1
    if slice_timing_difference is not None:
        params["slice_timing_difference"] = slice_timing_difference
    if slice_band is not None:
        params["slice_band"] = slice_band
    if flip_angle is not None:
        params["flip_angle"] = flip_angle
    if fsl_anat_dir is not None:
        params["fsl_anat_dir"] = fsl_anat_dir
    if structural_image is not None:
        params["structural_image"] = structural_image
    if bet_structural_image is not None:
        params["bet_structural_image"] = bet_structural_image
    if fast_segmentation_images is not None:
        params["fast_segmentation_images"] = fast_segmentation_images
    if precomputed_m0_value is not None:
        params["precomputed_m0_value"] = precomputed_m0_value
    if inversion_efficiency is not None:
        params["inversion_efficiency"] = inversion_efficiency
    if tr_calibration_data is not None:
        params["tr_calibration_data"] = tr_calibration_data
    if calibration_image is not None:
        params["calibration_image"] = calibration_image
    if calibration_method is not None:
        params["calibration_method"] = calibration_method
    return params


def oxford_asl_cargs(
    params: OxfordAslParameters,
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
    cargs.append("oxford_asl")
    cargs.extend([
        "-i",
        execution.input_file(params.get("asl_data"))
    ])
    cargs.extend([
        "-o",
        params.get("output_dir_name")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask"))
        ])
    if params.get("spatial_smoothing"):
        cargs.append("--spatial")
    if params.get("white_paper_analysis"):
        cargs.append("--wp")
    if params.get("motion_correction"):
        cargs.append("--mc")
    if params.get("input_asl_format") is not None:
        cargs.extend([
            "--iaf",
            params.get("input_asl_format")
        ])
    if params.get("input_block_format") is not None:
        cargs.extend([
            "--ibf",
            params.get("input_block_format")
        ])
    if params.get("inversion_times") is not None:
        cargs.extend([
            "--tis",
            params.get("inversion_times")
        ])
    if params.get("ti_image") is not None:
        cargs.extend([
            "--tiimg",
            execution.input_file(params.get("ti_image"))
        ])
    if params.get("casl"):
        cargs.append("--casl")
    if params.get("arterial_suppression"):
        cargs.append("--artsupp")
    if params.get("bolus_duration") is not None:
        cargs.extend([
            "--bolus",
            str(params.get("bolus_duration"))
        ])
    if params.get("bat") is not None:
        cargs.extend([
            "--bat",
            str(params.get("bat"))
        ])
    if params.get("tissue_t1") is not None:
        cargs.extend([
            "--t1",
            str(params.get("tissue_t1"))
        ])
    if params.get("blood_t1") is not None:
        cargs.extend([
            "--t1b",
            str(params.get("blood_t1"))
        ])
    if params.get("slice_timing_difference") is not None:
        cargs.extend([
            "--slicedt",
            str(params.get("slice_timing_difference"))
        ])
    if params.get("slice_band") is not None:
        cargs.extend([
            "--sliceband",
            str(params.get("slice_band"))
        ])
    if params.get("flip_angle") is not None:
        cargs.extend([
            "--fa",
            str(params.get("flip_angle"))
        ])
    if params.get("fsl_anat_dir") is not None:
        cargs.extend([
            "--fslanat",
            params.get("fsl_anat_dir")
        ])
    if params.get("structural_image") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("structural_image"))
        ])
    if params.get("bet_structural_image") is not None:
        cargs.extend([
            "--sbrain",
            execution.input_file(params.get("bet_structural_image"))
        ])
    if params.get("fast_segmentation_images") is not None:
        cargs.extend([
            "--fastsrc",
            params.get("fast_segmentation_images")
        ])
    if params.get("sensitivity_correction"):
        cargs.append("--senscorr")
    if params.get("precomputed_m0_value") is not None:
        cargs.extend([
            "--M0",
            str(params.get("precomputed_m0_value"))
        ])
    if params.get("inversion_efficiency") is not None:
        cargs.extend([
            "--alpha",
            str(params.get("inversion_efficiency"))
        ])
    if params.get("tr_calibration_data") is not None:
        cargs.extend([
            "--tr",
            str(params.get("tr_calibration_data"))
        ])
    if params.get("calibration_image") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("calibration_image"))
        ])
    if params.get("calibration_method") is not None:
        cargs.extend([
            "--cmethod",
            params.get("calibration_method")
        ])
    return cargs


def oxford_asl_outputs(
    params: OxfordAslParameters,
    execution: Execution,
) -> OxfordAslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = OxfordAslOutputs(
        root=execution.output_file("."),
        output_dir=execution.output_file(params.get("output_dir_name")),
    )
    return ret


def oxford_asl_execute(
    params: OxfordAslParameters,
    execution: Execution,
) -> OxfordAslOutputs:
    """
    Calculate perfusion maps from ASL data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `OxfordAslOutputs`).
    """
    params = execution.params(params)
    cargs = oxford_asl_cargs(params, execution)
    ret = oxford_asl_outputs(params, execution)
    execution.run(cargs)
    return ret


def oxford_asl(
    asl_data: InputPathType,
    output_dir_name: str,
    mask: InputPathType | None = None,
    spatial_smoothing: bool = False,
    white_paper_analysis: bool = False,
    motion_correction: bool = False,
    input_asl_format: str | None = None,
    input_block_format: str | None = None,
    inversion_times: str | None = None,
    ti_image: InputPathType | None = None,
    casl: bool = False,
    arterial_suppression: bool = False,
    bolus_duration: float | None = None,
    bat: float | None = None,
    tissue_t1: float | None = None,
    blood_t1: float | None = None,
    slice_timing_difference: float | None = None,
    slice_band: float | None = None,
    flip_angle: float | None = None,
    fsl_anat_dir: str | None = None,
    structural_image: InputPathType | None = None,
    bet_structural_image: InputPathType | None = None,
    fast_segmentation_images: str | None = None,
    sensitivity_correction: bool = False,
    precomputed_m0_value: float | None = None,
    inversion_efficiency: float | None = None,
    tr_calibration_data: float | None = None,
    calibration_image: InputPathType | None = None,
    calibration_method: str | None = None,
    runner: Runner | None = None,
) -> OxfordAslOutputs:
    """
    Calculate perfusion maps from ASL data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        asl_data: Input ASL data.
        output_dir_name: Output directory name.
        mask: Mask in native space of ASL data.
        spatial_smoothing: Use adaptive spatial smoothing on perfusion.
        white_paper_analysis: Analysis that conforms to the 'white paper'\
            (Alsop et al. 2014).
        motion_correction: Apply motion correction using mcflirt.
        input_asl_format: Input ASL format: diff, tc, ct.
        input_block_format: Input block format (for multi-TI): rpt, tis.
        inversion_times: Comma separated list of inversion times.
        ti_image: 4D image containing voxelwise TI values.
        casl: ASL acquisition is pseudo cASL (pcASL) rather than pASL.
        arterial_suppression: Arterial suppression (vascular crushing) was used.
        bolus_duration: Bolus duration.
        bat: Bolus arrival time.
        tissue_t1: Tissue T1 value.
        blood_t1: Blood T1 value.
        slice_timing_difference: Timing difference between slices.
        slice_band: Number of slices per band in a multi-band setup.
        flip_angle: Flip angle for Look-Locker readout correction.
        fsl_anat_dir: An fsl_anat directory from structural image.
        structural_image: Structural image (whole head).
        bet_structural_image: Structural image (already BETed).
        fast_segmentation_images: Images from a FAST segmentation.
        sensitivity_correction: Use bias field (from segmentation) for\
            sensitivity correction.
        precomputed_m0_value: Single precomputed M0 value.
        inversion_efficiency: Inversion efficiency.
        tr_calibration_data: TR of calibration data.
        calibration_image: M0 calibration image (proton density or mean control\
            image).
        calibration_method: Calibration method: single or voxel.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `OxfordAslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(OXFORD_ASL_METADATA)
    params = oxford_asl_params(
        asl_data=asl_data,
        output_dir_name=output_dir_name,
        mask=mask,
        spatial_smoothing=spatial_smoothing,
        white_paper_analysis=white_paper_analysis,
        motion_correction=motion_correction,
        input_asl_format=input_asl_format,
        input_block_format=input_block_format,
        inversion_times=inversion_times,
        ti_image=ti_image,
        casl=casl,
        arterial_suppression=arterial_suppression,
        bolus_duration=bolus_duration,
        bat=bat,
        tissue_t1=tissue_t1,
        blood_t1=blood_t1,
        slice_timing_difference=slice_timing_difference,
        slice_band=slice_band,
        flip_angle=flip_angle,
        fsl_anat_dir=fsl_anat_dir,
        structural_image=structural_image,
        bet_structural_image=bet_structural_image,
        fast_segmentation_images=fast_segmentation_images,
        sensitivity_correction=sensitivity_correction,
        precomputed_m0_value=precomputed_m0_value,
        inversion_efficiency=inversion_efficiency,
        tr_calibration_data=tr_calibration_data,
        calibration_image=calibration_image,
        calibration_method=calibration_method,
    )
    return oxford_asl_execute(params, execution)


__all__ = [
    "OXFORD_ASL_METADATA",
    "OxfordAslOutputs",
    "OxfordAslParameters",
    "oxford_asl",
    "oxford_asl_params",
]
