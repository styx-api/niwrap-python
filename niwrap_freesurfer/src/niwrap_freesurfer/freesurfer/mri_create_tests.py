# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CREATE_TESTS_METADATA = Metadata(
    id="999792ae56910fc6d041db101d550da0a7da203a.boutiques",
    name="mri_create_tests",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCreateTestsParameters = typing.TypedDict('MriCreateTestsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_create_tests"],
    "input_file": InputPathType,
    "out_src": str,
    "out_target": str,
    "input_target": typing.NotRequired[InputPathType | None],
    "lta_in": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "noise": typing.NotRequired[float | None],
    "outlier": typing.NotRequired[float | None],
    "outlier_box": typing.NotRequired[float | None],
    "translation_flag": bool,
    "transdist": typing.NotRequired[float | None],
    "rotation_flag": bool,
    "maxdeg": typing.NotRequired[float | None],
    "intensity_flag": bool,
    "iscale": typing.NotRequired[float | None],
    "lta_out": typing.NotRequired[str | None],
    "lta_outs": typing.NotRequired[str | None],
    "lta_outt": typing.NotRequired[str | None],
    "iscale_out": typing.NotRequired[str | None],
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
        "mri_create_tests": mri_create_tests_cargs,
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
    }.get(t)


class MriCreateTestsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_create_tests(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_create_tests_params(
    input_file: InputPathType,
    out_src: str,
    out_target: str,
    input_target: InputPathType | None = None,
    lta_in: str | None = None,
    mask: InputPathType | None = None,
    noise: float | None = None,
    outlier: float | None = None,
    outlier_box: float | None = None,
    translation_flag: bool = False,
    transdist: float | None = None,
    rotation_flag: bool = False,
    maxdeg: float | None = None,
    intensity_flag: bool = False,
    iscale: float | None = None,
    lta_out: str | None = None,
    lta_outs: str | None = None,
    lta_outt: str | None = None,
    iscale_out: str | None = None,
) -> MriCreateTestsParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input volume to be modified.
        out_src: Output source volume name.
        out_target: Output target volume name.
        input_target: Input target volume to be modified, must be in the same\
            space as input volume. Default: use input volume to create output\
            target.
        lta_in: Specify LTA for mapping input to output target. Cannot be used\
            with --rotation or --translation.
        mask: Mask source MRI with mask file.
        noise: Add global Gaussian noise.
        outlier: Add random outlier voxels.
        outlier_box: Add box containing random voxels.
        translation_flag: Apply random translation.
        transdist: Set maximal translation distance in mm. Default is 11.
        rotation_flag: Apply random rotation.
        maxdeg: Maximal rotation in degrees. Default is 25.
        intensity_flag: Apply random intensity scaling.
        iscale: Use fixed intensity scaling parameter.
        lta_out: Write used random transform to LTA.
        lta_outs: Write halfway LTA for source.
        lta_outt: Write halfway LTA for target.
        iscale_out: Write used intensity scaling parameter.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_create_tests",
        "input_file": input_file,
        "out_src": out_src,
        "out_target": out_target,
        "translation_flag": translation_flag,
        "rotation_flag": rotation_flag,
        "intensity_flag": intensity_flag,
    }
    if input_target is not None:
        params["input_target"] = input_target
    if lta_in is not None:
        params["lta_in"] = lta_in
    if mask is not None:
        params["mask"] = mask
    if noise is not None:
        params["noise"] = noise
    if outlier is not None:
        params["outlier"] = outlier
    if outlier_box is not None:
        params["outlier_box"] = outlier_box
    if transdist is not None:
        params["transdist"] = transdist
    if maxdeg is not None:
        params["maxdeg"] = maxdeg
    if iscale is not None:
        params["iscale"] = iscale
    if lta_out is not None:
        params["lta_out"] = lta_out
    if lta_outs is not None:
        params["lta_outs"] = lta_outs
    if lta_outt is not None:
        params["lta_outt"] = lta_outt
    if iscale_out is not None:
        params["iscale_out"] = iscale_out
    return params


def mri_create_tests_cargs(
    params: MriCreateTestsParameters,
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
    cargs.append("mri_create_tests")
    cargs.extend([
        "--in",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "--outs",
        params.get("out_src")
    ])
    cargs.extend([
        "--outt",
        params.get("out_target")
    ])
    if params.get("input_target") is not None:
        cargs.extend([
            "--int",
            execution.input_file(params.get("input_target"))
        ])
    if params.get("lta_in") is not None:
        cargs.extend([
            "--lta-in",
            params.get("lta_in")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("noise") is not None:
        cargs.extend([
            "--noise",
            str(params.get("noise"))
        ])
    if params.get("outlier") is not None:
        cargs.extend([
            "--outlier",
            str(params.get("outlier"))
        ])
    if params.get("outlier_box") is not None:
        cargs.extend([
            "--outlier-box",
            str(params.get("outlier_box"))
        ])
    if params.get("translation_flag"):
        cargs.append("--translation")
    if params.get("transdist") is not None:
        cargs.extend([
            "--transdist",
            str(params.get("transdist"))
        ])
    if params.get("rotation_flag"):
        cargs.append("--rotation")
    if params.get("maxdeg") is not None:
        cargs.extend([
            "--maxdeg",
            str(params.get("maxdeg"))
        ])
    if params.get("intensity_flag"):
        cargs.append("--intensity")
    if params.get("iscale") is not None:
        cargs.extend([
            "--iscale",
            str(params.get("iscale"))
        ])
    if params.get("lta_out") is not None:
        cargs.extend([
            "--lta-out",
            params.get("lta_out")
        ])
    if params.get("lta_outs") is not None:
        cargs.extend([
            "--lta-outs",
            params.get("lta_outs")
        ])
    if params.get("lta_outt") is not None:
        cargs.extend([
            "--lta-outt",
            params.get("lta_outt")
        ])
    if params.get("iscale_out") is not None:
        cargs.extend([
            "--iscale-out",
            params.get("iscale_out")
        ])
    return cargs


def mri_create_tests_outputs(
    params: MriCreateTestsParameters,
    execution: Execution,
) -> MriCreateTestsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCreateTestsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_create_tests_execute(
    params: MriCreateTestsParameters,
    execution: Execution,
) -> MriCreateTestsOutputs:
    """
    Creates test cases for the registration by mapping the input to a source (half
    way backward) and to a target (half way forward).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCreateTestsOutputs`).
    """
    params = execution.params(params)
    cargs = mri_create_tests_cargs(params, execution)
    ret = mri_create_tests_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_create_tests(
    input_file: InputPathType,
    out_src: str,
    out_target: str,
    input_target: InputPathType | None = None,
    lta_in: str | None = None,
    mask: InputPathType | None = None,
    noise: float | None = None,
    outlier: float | None = None,
    outlier_box: float | None = None,
    translation_flag: bool = False,
    transdist: float | None = None,
    rotation_flag: bool = False,
    maxdeg: float | None = None,
    intensity_flag: bool = False,
    iscale: float | None = None,
    lta_out: str | None = None,
    lta_outs: str | None = None,
    lta_outt: str | None = None,
    iscale_out: str | None = None,
    runner: Runner | None = None,
) -> MriCreateTestsOutputs:
    """
    Creates test cases for the registration by mapping the input to a source (half
    way backward) and to a target (half way forward).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input volume to be modified.
        out_src: Output source volume name.
        out_target: Output target volume name.
        input_target: Input target volume to be modified, must be in the same\
            space as input volume. Default: use input volume to create output\
            target.
        lta_in: Specify LTA for mapping input to output target. Cannot be used\
            with --rotation or --translation.
        mask: Mask source MRI with mask file.
        noise: Add global Gaussian noise.
        outlier: Add random outlier voxels.
        outlier_box: Add box containing random voxels.
        translation_flag: Apply random translation.
        transdist: Set maximal translation distance in mm. Default is 11.
        rotation_flag: Apply random rotation.
        maxdeg: Maximal rotation in degrees. Default is 25.
        intensity_flag: Apply random intensity scaling.
        iscale: Use fixed intensity scaling parameter.
        lta_out: Write used random transform to LTA.
        lta_outs: Write halfway LTA for source.
        lta_outt: Write halfway LTA for target.
        iscale_out: Write used intensity scaling parameter.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCreateTestsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CREATE_TESTS_METADATA)
    params = mri_create_tests_params(
        input_file=input_file,
        out_src=out_src,
        out_target=out_target,
        input_target=input_target,
        lta_in=lta_in,
        mask=mask,
        noise=noise,
        outlier=outlier,
        outlier_box=outlier_box,
        translation_flag=translation_flag,
        transdist=transdist,
        rotation_flag=rotation_flag,
        maxdeg=maxdeg,
        intensity_flag=intensity_flag,
        iscale=iscale,
        lta_out=lta_out,
        lta_outs=lta_outs,
        lta_outt=lta_outt,
        iscale_out=iscale_out,
    )
    return mri_create_tests_execute(params, execution)


__all__ = [
    "MRI_CREATE_TESTS_METADATA",
    "MriCreateTestsOutputs",
    "MriCreateTestsParameters",
    "mri_create_tests",
    "mri_create_tests_params",
]
