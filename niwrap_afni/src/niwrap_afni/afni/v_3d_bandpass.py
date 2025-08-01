# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_BANDPASS_METADATA = Metadata(
    id="85554b333e3bdcbc05fde6959f1cb444905c3dd7.boutiques",
    name="3dBandpass",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dBandpassParameters = typing.TypedDict('V3dBandpassParameters', {
    "__STYXTYPE__": typing.Literal["3dBandpass"],
    "prefix": typing.NotRequired[str | None],
    "automask": bool,
    "blur": typing.NotRequired[float | None],
    "despike": bool,
    "highpass": float,
    "lowpass": float,
    "in_file": InputPathType,
    "localPV": typing.NotRequired[float | None],
    "mask": typing.NotRequired[InputPathType | None],
    "nfft": typing.NotRequired[int | None],
    "no_detrend": bool,
    "normalize": bool,
    "notrans": bool,
    "orthogonalize_dset": typing.NotRequired[InputPathType | None],
    "orthogonalize_file": typing.NotRequired[list[InputPathType] | None],
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
    "tr": typing.NotRequired[float | None],
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
        "3dBandpass": v_3d_bandpass_cargs,
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
        "3dBandpass": v_3d_bandpass_outputs,
    }.get(t)


class V3dBandpassOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_bandpass(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output file from 3dbandpass."""


def v_3d_bandpass_params(
    highpass: float,
    lowpass: float,
    in_file: InputPathType,
    prefix: str | None = None,
    automask: bool = False,
    blur: float | None = None,
    despike: bool = False,
    local_pv: float | None = None,
    mask: InputPathType | None = None,
    nfft: int | None = None,
    no_detrend: bool = False,
    normalize: bool = False,
    notrans: bool = False,
    orthogonalize_dset: InputPathType | None = None,
    orthogonalize_file: list[InputPathType] | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    tr: float | None = None,
) -> V3dBandpassParameters:
    """
    Build parameters.
    
    Args:
        highpass: Highpass.
        lowpass: Lowpass.
        in_file: Input file to 3dbandpass.
        prefix: Prefix for output file.
        automask: Create a mask from the input dataset.
        blur: Blur (inside the mask only) with a filter width (fwhm) of 'fff'\
            millimeters.
        despike: Despike each time series before other processing. hopefully,\
            you don't actually need to do this, which is why it is optional.
        local_pv: Replace each vector by the local principal vector (aka first\
            singular vector) from a neighborhood of radius 'rrr' millimeters. note\
            that the pv time series is l2 normalized. this option is mostly for bob\
            cox to have fun with.
        mask: Mask file.
        nfft: Set the fft length [must be a legal value].
        no_detrend: Skip the quadratic detrending of the input that occurs\
            before the fft-based bandpassing. you would only want to do this if the\
            dataset had been detrended already in some other program.
        normalize: Make all output time series have l2 norm = 1 (i.e., sum of\
            squares = 1).
        notrans: Don't check for initial positive transients in the data. the\
            test is a little slow, so skipping it is ok, if you know the data time\
            series are transient-free.
        orthogonalize_dset: Orthogonalize each voxel to the corresponding voxel\
            time series in dataset 'fset', which must have the same spatial and\
            temporal grid structure as the main input dataset. at present, only one\
            '-dsort' option is allowed.
        orthogonalize_file: Also orthogonalize input to columns in f.1d.\
            multiple '-ort' options are allowed.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        tr: Set time step (tr) in sec [default=from dataset header].
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dBandpass",
        "automask": automask,
        "despike": despike,
        "highpass": highpass,
        "lowpass": lowpass,
        "in_file": in_file,
        "no_detrend": no_detrend,
        "normalize": normalize,
        "notrans": notrans,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if blur is not None:
        params["blur"] = blur
    if local_pv is not None:
        params["localPV"] = local_pv
    if mask is not None:
        params["mask"] = mask
    if nfft is not None:
        params["nfft"] = nfft
    if orthogonalize_dset is not None:
        params["orthogonalize_dset"] = orthogonalize_dset
    if orthogonalize_file is not None:
        params["orthogonalize_file"] = orthogonalize_file
    if outputtype is not None:
        params["outputtype"] = outputtype
    if tr is not None:
        params["tr"] = tr
    return params


def v_3d_bandpass_cargs(
    params: V3dBandpassParameters,
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
    cargs.append("3dBandpass")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("blur") is not None:
        cargs.extend([
            "-blur",
            str(params.get("blur"))
        ])
    if params.get("despike"):
        cargs.append("-despike")
    cargs.append(str(params.get("highpass")))
    cargs.append(str(params.get("lowpass")))
    cargs.append(execution.input_file(params.get("in_file")))
    if params.get("localPV") is not None:
        cargs.extend([
            "-localPV",
            str(params.get("localPV"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("nfft") is not None:
        cargs.extend([
            "-nfft",
            str(params.get("nfft"))
        ])
    if params.get("no_detrend"):
        cargs.append("-nodetrend")
    if params.get("normalize"):
        cargs.append("-norm")
    if params.get("notrans"):
        cargs.append("-notrans")
    if params.get("orthogonalize_dset") is not None:
        cargs.extend([
            "-dsort",
            execution.input_file(params.get("orthogonalize_dset"))
        ])
    if params.get("orthogonalize_file") is not None:
        cargs.extend([
            "-ort",
            *[execution.input_file(f) for f in params.get("orthogonalize_file")]
        ])
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    if params.get("tr") is not None:
        cargs.extend([
            "-dt",
            str(params.get("tr"))
        ])
    return cargs


def v_3d_bandpass_outputs(
    params: V3dBandpassParameters,
    execution: Execution,
) -> V3dBandpassOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dBandpassOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_bandpass_execute(
    params: V3dBandpassParameters,
    execution: Execution,
) -> V3dBandpassOutputs:
    """
    Program to lowpass and/or highpass each voxel time series in a dataset, offering
    more/different options than Fourier.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dBandpassOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_bandpass_cargs(params, execution)
    ret = v_3d_bandpass_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_bandpass(
    highpass: float,
    lowpass: float,
    in_file: InputPathType,
    prefix: str | None = None,
    automask: bool = False,
    blur: float | None = None,
    despike: bool = False,
    local_pv: float | None = None,
    mask: InputPathType | None = None,
    nfft: int | None = None,
    no_detrend: bool = False,
    normalize: bool = False,
    notrans: bool = False,
    orthogonalize_dset: InputPathType | None = None,
    orthogonalize_file: list[InputPathType] | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    tr: float | None = None,
    runner: Runner | None = None,
) -> V3dBandpassOutputs:
    """
    Program to lowpass and/or highpass each voxel time series in a dataset, offering
    more/different options than Fourier.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        highpass: Highpass.
        lowpass: Lowpass.
        in_file: Input file to 3dbandpass.
        prefix: Prefix for output file.
        automask: Create a mask from the input dataset.
        blur: Blur (inside the mask only) with a filter width (fwhm) of 'fff'\
            millimeters.
        despike: Despike each time series before other processing. hopefully,\
            you don't actually need to do this, which is why it is optional.
        local_pv: Replace each vector by the local principal vector (aka first\
            singular vector) from a neighborhood of radius 'rrr' millimeters. note\
            that the pv time series is l2 normalized. this option is mostly for bob\
            cox to have fun with.
        mask: Mask file.
        nfft: Set the fft length [must be a legal value].
        no_detrend: Skip the quadratic detrending of the input that occurs\
            before the fft-based bandpassing. you would only want to do this if the\
            dataset had been detrended already in some other program.
        normalize: Make all output time series have l2 norm = 1 (i.e., sum of\
            squares = 1).
        notrans: Don't check for initial positive transients in the data. the\
            test is a little slow, so skipping it is ok, if you know the data time\
            series are transient-free.
        orthogonalize_dset: Orthogonalize each voxel to the corresponding voxel\
            time series in dataset 'fset', which must have the same spatial and\
            temporal grid structure as the main input dataset. at present, only one\
            '-dsort' option is allowed.
        orthogonalize_file: Also orthogonalize input to columns in f.1d.\
            multiple '-ort' options are allowed.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        tr: Set time step (tr) in sec [default=from dataset header].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBandpassOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BANDPASS_METADATA)
    params = v_3d_bandpass_params(
        prefix=prefix,
        automask=automask,
        blur=blur,
        despike=despike,
        highpass=highpass,
        lowpass=lowpass,
        in_file=in_file,
        local_pv=local_pv,
        mask=mask,
        nfft=nfft,
        no_detrend=no_detrend,
        normalize=normalize,
        notrans=notrans,
        orthogonalize_dset=orthogonalize_dset,
        orthogonalize_file=orthogonalize_file,
        outputtype=outputtype,
        tr=tr,
    )
    return v_3d_bandpass_execute(params, execution)


__all__ = [
    "V3dBandpassOutputs",
    "V3dBandpassParameters",
    "V_3D_BANDPASS_METADATA",
    "v_3d_bandpass",
    "v_3d_bandpass_params",
]
